def newton_raphson(f, f_prime, x0, tol, max_iter):
  """
  Implementa el método de Newton-Raphson para encontrar la raíz de una función.

  Parámetros:
    f: La función a evaluar.
    f_prime: La derivada de la función f.
    x0: El valor inicial.
    tol: La tolerancia de error.
    max_iter: El número máximo de iteraciones.

  Retorno:
    La raíz de la función.
  """
  
  # Inicialización
  x_prev = x0
  i = 0
  
  # Bucle de iteración
  while abs(f(x_prev)) > tol and i < max_iter:
    x_next = x_prev - f(x_prev) / f_prime(x_prev)
    x_prev = x_next
    i += 1
  
  # Validación de convergencia
  if i == max_iter:
    print(f"No se encontró la raíz en {max_iter} iteraciones.")
    return None
  else:
    return x_next

# Ejemplo de uso
def f(x):
  return x**2 - 5

def f_prime(x):
  return 2*x

x0 = 2
tol = 1e-5
max_iter = 100

root = newton_raphson(f, f_prime, x0, tol, max_iter)

if root is not None:
  print(f"La raíz de la función es: {root}")

