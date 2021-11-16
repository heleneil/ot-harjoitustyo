import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_oikein_alussa(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_lataa_rahaa_toimii_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.2")
    
    def test_ota_rahaa_toimii_oikein(self):
        self.maksukortti.ota_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")

    def test_ei_ota_rahaa_jos_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(20)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_metodi_palauttaa_true(self):
        ota_rahaa_result = self.maksukortti.ota_rahaa(10)
        self.assertTrue(ota_rahaa_result)

    def test_metodi_palauttaa_false(self):
        ota_rahaa_result = self.maksukortti.ota_rahaa(100)
        self.assertFalse(ota_rahaa_result)