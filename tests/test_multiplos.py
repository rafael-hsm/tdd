from multiplos import numeros_multiplos
import unittest


class test_numeros_multiplos(unittest.TestCase):

    def test_multiplos_24_6(self):
        self.assertEqual(numeros_multiplos(24, 6), 'sao multiplos')

    def test_multiplos_6_24(self):
        self.assertEqual(numeros_multiplos(6, 24), 'sao multiplos')

    def test_multiplos_25_5(self):
        self.assertEqual(numeros_multiplos(25, 5), 'sao multiplos')

    def test_multiplos_5_25(self):
        self.assertEqual(numeros_multiplos(5, 25), 'sao multiplos')

    def test_multiplos_25_6(self):
        self.assertEqual(numeros_multiplos(25, 6),'nao sao multiplos')

    def test_multiplos_6_25(self):
        self.assertEqual(numeros_multiplos(6, 25), 'nao sao multiplos')

    def test_multiplos_15_3(self):
        self.assertEqual(numeros_multiplos(15, 3), 'sao multiplos')

    def test_multipplos_15_5(self):
        self.assertEqual(numeros_multiplos(15, 5), 'sao multiplos')

    def test_multiplos_15_2(self):
        self.assertEqual(numeros_multiplos(15, 2), 'nao sao multiplos')

