def maze_distance(maze, start, end):
    """
    Calcula la distancia en un laberinto entre dos puntos utilizando búsqueda en anchura (BFS).

    Parametros:
    maze (list): Laberinto representado como una matriz de 0s y 1s, donde 0 representa un camino bloqueado y 1 un camino abierto.
    start (tuple): Coordenadas (fila, columna) del punto de inicio.
    end (tuple): Coordenadas (fila, columna) del punto de fin.

    Retorna:
    int: Distancia en el laberinto entre los puntos de inicio y fin.
    """
    rows, cols = len(maze), len(maze[0])
    visited = [[False] * cols for _ in range(rows)]

    queue = [(start, 0)]  # Cola para BFS: (coordenadas, distancia)

    while queue:
        (row, col), distance = queue.pop(0)
        
        if (row, col) == end:
            return distance

        visited[row][col] = True

        # Movimientos: arriba, abajo, izquierda, derecha
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            
            if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == 1 and not visited[new_row][new_col]:
                queue.append(((new_row, new_col), distance + 1))

    return -1  # Si no se puede llegar al punto de fin


# Ejemplo de uso
maze_example = [[1, 0, 1, 1, 1],
                [1, 1, 1, 0, 1],
                [0, 0, 1, 1, 1],
                [1, 1, 1, 1, 1]]

start_point = (0, 0)
end_point = (3, 4)

distance = maze_distance(maze_example, start_point, end_point)
if distance != -1:
    print("La distancia en el laberinto es:", distance)
else:
    print("No se puede llegar al punto de fin en el laberinto.")
