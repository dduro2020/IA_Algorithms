import heapq

def ucs(grid, start, goal):
    """
    Implementa el algoritmo de Búsqueda con Coste Uniforme (UCS) para búsqueda de caminos.

    Parametros:
    grid (list): La cuadrícula representada como una lista de listas donde 1 es un camino abierto y 0 es un obstáculo.
    start (tuple): Coordenadas (fila, columna) del punto de inicio.
    goal (tuple): Coordenadas (fila, columna) del punto de fin.

    Retorna:
    list: Lista de coordenadas que representan la ruta desde el punto de inicio hasta el punto de fin.
    """
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    distances = [[float('inf')] * cols for _ in range(rows)]
    parent = [[None] * cols for _ in range(rows)]
    
    heap = [(0, start)]  # Montículo para UCS: (costo acumulado, coordenadas)
    
    while heap:
        cost, current = heapq.heappop(heap)
        row, col = current
        
        if current == goal:
            # Reconstruye y devuelve la ruta
            path = []
            while current:
                path.append(current)
                current = parent[row][col]
                if current:
                    row, col = current
        
            return path[::-1]
        
        if visited[row][col]:
            continue
        
        visited[row][col] = True
        
        # Movimientos: abajo, derecha, arriba, izquierda
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            
            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                new_cost = cost + 1  # Costo uniforme, en este caso siempre es 1
                
                if new_cost < distances[new_row][new_col]:
                    distances[new_row][new_col] = new_cost
                    heapq.heappush(heap, (new_cost, (new_row, new_col)))
                    parent[new_row][new_col] = current
    
    return None


# Ejemplo de uso
grid = [[1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]]

start = (0, 0)
goal = (3, 4)

path = ucs(grid, start, goal)

if path:
    print("Ruta encontrada (UCS):", path)
else:
    print("No se encontró una ruta (UCS).")
