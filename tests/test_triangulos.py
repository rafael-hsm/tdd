import unittest
from tipos_triangulos import triangulos, ordena_lados


class TestTriangulo(unittest.TestCase):
    def test_ordena_lados(self):
        self.assertEqual(ordena_lados(7.0, 5.0, 6.0), [7.0, 6.0, 5.0])

    def test_triangulo_retangulo(self):
        self.assertEqual(triangulos(6.0, 8.0, 10.0), 'TRIANGULO RETANGULO')

    def test_nao_triangulo(self):
        self.assertEqual(triangulos(5.0, 7.0, 2.0), 'NAO FORMA TRIANGULO')

    def test_triangulo_acutangulo(self):
        self.assertEqual(triangulos(7.0, 5.0, 6.0), 'TRIANGULO ACUTANGULO')

    def test_triangulo_acutangulo_isosceles(self):
        self.assertEqual(triangulos(7.0, 5.0, 7.0), 'TRIANGULO ACUTANGULO ISOSCELES')

    def test_triangulo_acutangulo_equilatero(self):
        self.assertEqual(triangulos(7.0, 7.0, 7.0), 'TRIANGULO ACUTANGULO EQUILATERO')

    def test_triangulo_obtusangulo(self):
        self.assertEqual(triangulos(6.0, 5.0, 10.0), 'TRIANGULO OBTUSANGULO')

    def test_triangulo_obtusangulo_isosceles(self):
        self.assertEqual(triangulos(6.0, 6.0, 10.0), 'TRIANGULO OBTUSANGULO ISOSCELES') 
