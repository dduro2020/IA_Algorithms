def greedy_search(grid, start, goal):
    """
    Implementa un algoritmo voraz para búsqueda de caminos.

    Parametros:
    grid (list): La cuadrícula representada como una lista de listas donde 1 es un camino abierto y 0 es un obstáculo.
    start (tuple): Coordenadas (fila, columna) del punto de inicio.
    goal (tuple): Coordenadas (fila, columna) del punto de fin.

    Retorna:
    list: Lista de coordenadas que representan la ruta desde el punto de inicio hasta el punto de fin.
    """
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    
    # Creamos una pila para DFS: (coordenadas, ruta)
    stack = [(start, [start])]
    
    while stack:
        current, path = stack.pop()
        row, col = current
        
        if current == goal:
            return path  # Ruta encontrada
        
        visited[row][col] = True
        
        # Movimientos: abajo, derecha, arriba, izquierda
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        # Ordenar los movimientos por cercanía al objetivo
        moves.sort(key=lambda move: abs(goal[0] - (row + move[0])) + abs(goal[1] - (col + move[1])))
        
        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            
            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1 and not visited[new_row][new_col]:
                stack.append(((new_row, new_col), path + [(new_row, new_col)]))
    
    return None


# Ejemplo de uso
grid = [[1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]]

start = (0, 0)
goal = (3, 4)

path = greedy_search(grid, start, goal)

if path:
    print("Ruta encontrada (Greedy Search):", path)
else:
    print("No se encontró una ruta (Greedy Search).")
