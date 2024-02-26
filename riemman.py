def riemann_integral(f, a, b, n):
    dx = (b - a) / n
    suma = 0.0
    x = a
    for i in range(n):
        suma += f(x) * dx
        x += dx
    return suma
