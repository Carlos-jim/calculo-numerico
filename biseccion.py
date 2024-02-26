def biseccion(f, a, b, tol=1e-6):
    if f(a) * f(b) > 0:
        raise ValueError("La función debe tener signos opuestos en a y b")

    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0

        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return print("biseccion;", (a + b) / 2.0)
