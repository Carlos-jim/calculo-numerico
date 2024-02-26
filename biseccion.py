def metodo_biseccion(funcion, a, b, tolerancia):
  """
  Implementa el método de bisección para encontrar la raíz de una función.

  Parámetros:
    funcion: La función a evaluar.
    a: El extremo izquierdo del intervalo.
    b: El extremo derecho del intervalo.
    tolerancia: La tolerancia de error para la aproximación de la raíz.

  Retorno:
    Una tupla que contiene la aproximación de la raíz y el número de iteraciones.
  """
  
  # Validar que la función sea continua en el intervalo
  if funcion(a) * funcion(b) > 0:
    raise ValueError("La función no es continua en el intervalo")

  # Inicializar variables
  fa = funcion(a)
  fb = funcion(b)
  iteraciones = 0

  while abs(b - a) > tolerancia:
    # Calcular el punto medio del intervalo
    c = (a + b) / 2

    # Evaluar la función en el punto medio
    fc = funcion(c)

    # Actualizar los intervalos
    if fa * fc < 0:
      b = c
    else:
      a = c

    # Actualizar el número de iteraciones
    iteraciones += 1

  # Calcular la aproximación de la raíz
  raiz = (a + b) / 2

  return raiz, iteraciones

# Función a evaluar
def f(x):
  return x**2 - 2

# Parámetros del método
a = 0
b = 2
tolerancia = 1e-6

# Aplicar el método de bisección
raiz, iteraciones = metodo_biseccion(f, a, b, tolerancia)

# Imprimir los resultados
print(f"Raíz aproximada: {raiz}")
print(f"Número de iteraciones: {iteraciones}")
