"""Testes locais sinteticos; nenhuma operacao SEI."""
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from fila_local import connect, prepare, reserve, reconcile, digest
from test_decidir_etapa import ready


class QueueTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.path=Path(self.temp.name)
        self.pdf=self.path/'test.pdf'; self.pdf.write_bytes(b'%PDF-1.4 synthetic test only')
        self.db=connect(self.path/'queue.sqlite')
        self.item={'nup':'00000.000001/2026-00','placa':'AAA0000','arquivo':str(self.pdf)}
        self.key=prepare(self.db,[self.item])[0]
        self.control=ready(); self.control['arquivo_sha256']=digest(self.pdf)

    def tearDown(self):
        self.db.close(); self.temp.cleanup()

    def test_idempotent_prepare(self):
        prepare(self.db,[self.item,self.item])
        self.assertEqual(self.db.execute('SELECT count(*) FROM itens').fetchone()[0],1)

    def test_atomic_rollback_conflicting_batch(self):
        another=dict(self.item,nup='00000.000002/2026-00')
        with self.assertRaises(ValueError): prepare(self.db,[another])
        self.assertEqual(self.db.execute('SELECT count(*) FROM itens').fetchone()[0],1)

    def test_double_reservation_across_connections(self):
        reserve(self.db,self.key,self.control)
        other=connect(self.path/'queue.sqlite')
        try:
            with self.assertRaises(ValueError): reserve(other,self.key,self.control)
        finally: other.close()

    def test_file_changed(self):
        self.pdf.write_bytes(b'%PDF-1.4 changed')
        with self.assertRaises(ValueError): reserve(self.db,self.key,self.control)

    def test_wrong_identity(self):
        self.control['placa']='BBB0000'
        with self.assertRaises(ValueError): reserve(self.db,self.key,self.control)

    def test_stop_request(self):
        self.control['parar']=True
        with self.assertRaises(ValueError): reserve(self.db,self.key,self.control)

    def test_uncertain_never_retries(self):
        reserve(self.db,self.key,self.control)
        reconcile(self.db,self.key,'INCERTA','Fixture timeout')
        with self.assertRaises(ValueError): reserve(self.db,self.key,self.control)

    def test_mismatched_readback_does_not_finalize(self):
        reserve(self.db,self.key,self.control)
        bad=self.path/'bad.pdf'; bad.write_bytes(b'%PDF-1.4 other')
        with self.assertRaises(ValueError): reconcile(self.db,self.key,'INCLUIDO','Fixture','123',bad)
        self.assertEqual(self.db.execute('SELECT estado FROM itens').fetchone()[0],'INICIADA')

    def test_verified_and_history_retained(self):
        reserve(self.db,self.key,self.control)
        reconcile(self.db,self.key,'INCLUIDO','Fixture: same NUP; readback', '123',self.pdf)
        self.assertEqual(self.db.execute('SELECT count(*) FROM eventos').fetchone()[0],3)
        with self.assertRaises(ValueError): reconcile(self.db,self.key,'SEM_EFEITO','Invalid rollback')

    def test_existing_without_upload(self):
        reconcile(self.db,self.key,'JA_EXISTENTE','Fixture readback', '123',self.pdf)
        with self.assertRaises(ValueError): reserve(self.db,self.key,self.control)

    def test_new_pdf_same_nup_blocked_while_uncertain(self):
        reserve(self.db,self.key,self.control)
        another=self.path/'other.pdf'; another.write_bytes(b'%PDF-1.4 new date')
        key=prepare(self.db,[dict(self.item,arquivo=str(another))])[0]
        self.control['arquivo_sha256']=digest(another)
        with self.assertRaises(ValueError): reserve(self.db,key,self.control)


if __name__=='__main__': unittest.main()
