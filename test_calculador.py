import unittest
import calculador

class TestCalculador(unittest.TestCase):
    def test_sumar(self):
        resultado = calculador.sumar(20, 17)
        self.assertEqual(resultado, 37)

    def test_restar(self):
        resultado = calculador.restar(3, 7)
        self.assertEqual(resultado, -4)

    def test_multiplicar(self):
        resultado = calculador.multiplicar(11, 4)
        self.assertEqual(resultado, 44)

    def test_dividir(self):
        resultado = calculador.dividir(6, 3)
        self.assertEqual(resultado, 2)
        
        with self.assertRaises(ZeroDivisionError):
            calculador.dividir(10, 0)

if __name__ == "__main__":
    unittest.main()
