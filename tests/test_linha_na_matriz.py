"""Teste do programa linha_na_matriz. Uri-1181"""
from linha_na_matriz import linha_na_matriz
from unittest import TestCase


class TestLinhaNaMatriz(TestCase):
    def test_soma_linha_2(self):
        self.assertEqual(linha_na_matriz(2, 'S'), 64.7)


    def test_soma_linha_5(self):
        self.assertEqual(linha_na_matriz(5, 'S'), 78.0)


    def test_media_linha5(self):
        self.assertEqual(linha_na_matriz(5, 'M'), 6.5)


    def test_media_linha7(self):
        self.assertEqual(linha_na_matriz(7, 'M'), 1.0)