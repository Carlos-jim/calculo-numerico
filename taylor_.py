def factorial(n):
  """
  Calcula el factorial de un número.

  Parámetros:
    n: El número a calcular el factorial.

  Retorno:
    El factorial de n.
  """
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

def derivada_n(f, x, n):
  """
  Calcula la derivada n-ésima de una función en un punto.

  Parámetros:
    f: La función a calcular la derivada.
    x: El punto en el que se calcula la derivada.
    n: El orden de la derivada.

  Retorno:
    El valor de la derivada n-ésima de f en x.
  """
  if n == 0:
    return f(x)
  else:
    h = 1e-6
    return (derivada_n(f, x + h, n - 1) - derivada_n(f, x - h, n - 1)) / (2 * h)

def taylor(f, x, a, n):
  """
  Calcula el polinomio de Taylor de grado n de una función en un punto.

  Parámetros:
    f: La función a calcular el polinomio de Taylor.
    x: El punto en el que se calcula el polinomio de Taylor.
    a: El punto alrededor del cual se expande la serie de Taylor.
    n: El grado del polinomio de Taylor.

  Retorno:
    El valor del polinomio de Taylor de grado n de f en x.
  """
  suma = 0
  for i in range(n + 1):
    suma += (derivada_n(f, a, i) * (x - a)**i) / factorial(i)
  return suma

# Ejemplo de uso
def f(x):
  return x**2 + 3*x + 1

x = 2
a = 1
n = 3

resultado = taylor(f, x, a, n)

print(f"El valor del polinomio de Taylor de grado {n} de f en x = {x} es: {resultado}")
