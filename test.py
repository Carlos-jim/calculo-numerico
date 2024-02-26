import unittest
from biseccion import biseccion
from newtonraphson import newton_raphson
from taylor_ import factorial, derivada_n, taylor
from trapecio import integrar_trapecio
from riemman import riemann_integral

#Test biseccion
class TestBiseccion(unittest.TestCase):
    def test_biseccion(self):
        # Definimos una función para la prueba
        def f(x):
            return x**2 - 4

        # Usamos el método de bisección para encontrar la raíz
        raiz = biseccion(f, 1, 3, tol=1e-6)

        # Verificamos que la raíz sea correcta con una tolerancia
        self.assertAlmostEqual(raiz, 2, delta=1e-6)

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
  
#test Rieman
  class TestRiemannIntegral(unittest.TestCase):
    def test_riemann_integral(self):
        # Definimos una función simple para la prueba
        def f(x):
            return x**2

        # Calculamos la integral de x^2 de 0 a 1 con 1000 subdivisiones
        result = riemann_integral(f, 0, 1, 1000)

        # Sabemos que la integral exacta de x^2 de 0 a 1 es 1/3, así que comprobamos
        # que nuestro resultado está cerca de eso con alguna tolerancia
        self.assertAlmostEqual(result, 1/3, places=2)

if __name__ == '__main__':
    unittest.main()