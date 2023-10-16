from collections import deque

def is_valid_move(grid, visited, row, col):
    """
    Verifica si un movimiento a una celda específica es válido.

    Parámetros:
    grid (list): La cuadrícula representada como una lista de listas.
    visited (list): La matriz que indica si una celda ha sido visitada o no.
    row (int): La fila de la celda.
    col (int): La columna de la celda.

    Retorna:
    bool: True si el movimiento es válido, False en caso contrario.
    """
    rows, cols = len(grid), len(grid[0])
    return 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1 and not visited[row][col]

def bfs(grid, start, goal):
    """
    Implementa el algoritmo Breadth-First Search (BFS) para encontrar la ruta más corta entre dos puntos en una cuadrícula.

    Parámetros:
    grid (list): La cuadrícula representada como una lista de listas.
    start (tuple): Coordenadas (fila, columna) del punto de inicio.
    goal (tuple): Coordenadas (fila, columna) del punto de fin.

    Retorna:
    list: Lista de coordenadas que representan la ruta desde el punto de inicio hasta el punto de fin.
    """
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    parent = [[None for _ in range(cols)] for _ in range(rows)]
    
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True
    
    while queue:
        current_row, current_col = queue.popleft()
        
        if (current_row, current_col) == goal:
            # Reconstruye y devuelve la ruta
            path = []
            while (current_row, current_col) != start:
                path.append((current_row, current_col))
                current_row, current_col = parent[current_row][current_col]
            path.append(start)
            return path[::-1]
        
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = current_row + dr, current_col + dc
            
            if is_valid_move(grid, visited, new_row, new_col):
                queue.append((new_row, new_col))
                visited[new_row][new_col] = True
                parent[new_row][new_col] = (current_row, current_col)
    
    return None

# Ejemplo de uso
grid_bfs = [[1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]]

start_bfs = (0, 0)
goal_bfs = (3, 4)

path_bfs = bfs(grid_bfs, start_bfs, goal_bfs)

if path_bfs:
    print("Ruta encontrada (BFS):", path_bfs)
else:
    print("No se encontró una ruta (BFS).")
