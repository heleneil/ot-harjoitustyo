import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(400)

    def test_kassapaatteen_saldo_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_myytyjen_maukkaiden_lounaiden_maara_oikea(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_myytyjen_edullisten_lounaiden_maara_oikea(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_toimii(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100640)

    def test_maukkaan_kateisosto_takaisinmaksu_toimii(self):
        self.vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(440)
        self.assertEqual(self.vaihtoraha, 40)

    def test_edullisen_kateisosto_takaisinmaksu_toimii(self):
        self.vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(440)
        self.assertEqual(self.vaihtoraha, 200)

    def test_edullisten_lounaiden_maara_kasvaa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaiden_lounaiden_maara_kasvaa_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaiden_lounaiden_maara_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisten_lounaiden_maara_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_kateisosto_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_edullisesti_kateisosto_vaihtoraha_palautetaan(self):
        self.vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.vaihtoraha, 200)

    def test_syo_maukkaasti_kateisosto_vaihtoraha_palautetaan(self):
        self.vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.vaihtoraha, 300)

    def test_kortilla_osto_palauttaa_true_syo_edullisesti(self):
        self.korttiosto_tulos = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertTrue(self.korttiosto_tulos)

    def test_kortilla_osto_palauttaa_true_syo_maukkaasti(self):
        self.korttiosto_tulos = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertTrue(self.korttiosto_tulos)

    def test_korttiosto_myytyjen_maukkaiden_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttiosto_myytyjen_edullisten_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kortilla_ei_tarpeeksi_saldo_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 0)
   
    def test_kortilla_ei_tarpeeksi_palauttaa_false(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.korttiosto = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertFalse(self.korttiosto)

    def test_korttiosto_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataa_kortille_saldo_muuttuu(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.maksukortti.saldo, 500)

    def test_lataa_kortille_rahamaara_kassassa_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)