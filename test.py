import unittest
from biseccion import metodo_biseccion
from newtonraphson import newton_raphson
from taylor_ import factorial, derivada_n, taylor
from trapecio import integrar_trapecio

class TestMetodoBiseccion(unittest.TestCase):

  def test_funcion_continua(self):
    # Función continua
    def f(x):
      return x**2 - 2

    # Parámetros del método
    a = 0
    b = 2
    tolerancia = 1e-6

    # Aplicar el método de bisección
    raiz, iteraciones = metodo_biseccion(f, a, b, tolerancia)

    # Validar la aproximación de la raíz
    self.assertAlmostEqual(raiz, 1.414213562373095, places=6)

  def test_funcion_no_continua(self):
    # Función no continua
    def f(x):
      if x < 0.5:
        return 1
      else:
        return -1

    # Parámetros del método
    a = 0
    b = 1
    tolerancia = 1e-6

    with self.assertRaises(ValueError):
      metodo_biseccion(f, a, b, tolerancia)

if __name__ == "__main__":
  unittest.main()


#Test NewtonRaphson
class TestNewtonRaphson(unittest.TestCase):
  def test_convergence(self):
    def f(x):
      return x**2 - 5

    def f_prime(x):
      return 2*x

    x0 = 2
    tol = 1e-5
    max_iter = 100

    root = newton_raphson(f, f_prime, x0, tol, max_iter)

    self.assertAlmostEqual(root, 2.23606797749979)

if __name__ == "__main__":
  unittest.main()
  
  
  
#Test de Taylor 
class TestTaylor(unittest.TestCase):

  def test_factorial(self):
    self.assertEqual(factorial(0), 1)
    self.assertEqual(factorial(1), 1)
    self.assertEqual(factorial(2), 2)
    self.assertEqual(factorial(3), 6)
    self.assertEqual(factorial(4), 24)

  def test_derivada_n(self):
    def f(x):
      return x**2
    self.assertEqual(derivada_n(f, 1, 0), 2)
    self.assertEqual(derivada_n(f, 1, 1), 0)
    self.assertEqual(derivada_n(f, 1, 2), -2)

  def test_taylor(self):
    def f(x):
      return x**2 + 3*x + 1
    self.assertEqual(taylor(f, 2, 1, 3), 10)

if __name__ == "__main__":
  unittest.main()
  
class TestIntegracionTrapecio(unittest.TestCase):
  def test_funcion_lineal(self):
    def f(x):
      return x
    a = 0
    b = 1
    n = 10
    resultado_esperado = 0.5
    resultado_obtenido = integrar_trapecio(f, a, b, n)
    self.assertEqual(resultado_esperado, resultado_obtenido)

  def test_funcion_cuadratica(self):
    def f(x):
      return x**2
    a = 0
    b = 1
    n = 10
    resultado_esperado = 1/3
    resultado_obtenido = integrar_trapecio(f, a, b, n)
    self.assertEqual(resultado_esperado, resultado_obtenido)

if __name__ == "__main__":
  unittest.main()