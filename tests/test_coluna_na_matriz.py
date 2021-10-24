"""Teste do programa coluna_na_matriz. Uri-1182"""
from coluna_na_matriz import coluna_na_matriz
from unittest import TestCase


class test_coluna_na_matriz(TestCase):
    def test_soma_coluna_5(self):
        self.assertEqual(coluna_na_matriz(5, 'S'), 78.0)

    def test_media_coluna_5(self):
        self.assertEqual(coluna_na_matriz(5, 'M'), 6.5)
