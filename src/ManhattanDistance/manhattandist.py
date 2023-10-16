def manhattan_distance(point1, point2):
    """
    Calcula la distancia de Manhattan entre dos puntos en una cuadrícula.

    Parametros:
    point1 (tuple): Coordenadas (x, y) del primer punto.
    point2 (tuple): Coordenadas (x, y) del segundo punto.

    Retorna:
    int: Distancia de Manhattan entre los puntos.
    """
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)


# Ejemplo de uso
point1 = (0, 0)
point2 = (3, 4)

distance = manhattan_distance(point1, point2)
print("La distancia de Manhattan es:", distance)
