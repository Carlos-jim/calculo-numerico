def integrar_trapecio(f, a, b, n):
  """
  Calcula la integral definida de f entre a y b usando el método del trapecio con n subintervalos.

  Parámetros:
    f: La función a integrar.
    a: El límite inferior de la integral.
    b: El límite superior de la integral.
    n: El número de subintervalos.

  Retorno:
    El valor aproximado de la integral.
  """
  h = (b - a) / n
  sumatoria = 0.5 * (f(a) + f(b))
  for i in range(1, n):
    sumatoria += f(a + i * h)
  return h * sumatoria

# Ejemplo de uso
def f(x):
  return x**2

a = 0
b = 1
n = 10

resultado = integrar_trapecio(f, a, b, n)

print(f"Resultado trapecio: {resultado}")
