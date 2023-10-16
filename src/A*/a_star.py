import heapq

class Node:
    def __init__(self, position, parent=None):
        """
        Clase que representa un nodo en el algoritmo A*.

        Parámetros:
        position (tuple): Coordenadas (fila, columna) del nodo.
        parent (Node): Nodo padre en la ruta.

        Atributos:
        position (tuple): Coordenadas (fila, columna) del nodo.
        parent (Node): Nodo padre en la ruta.
        g (int): Costo acumulado desde el nodo inicial hasta este nodo.
        h (int): Heurística, estimación del costo restante desde este nodo hasta el nodo objetivo.
        """
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
    
    def __lt__(self, other):
        """
        Método utilizado para comparar nodos en la cola de prioridad.

        Parámetros:
        other (Node): Otro nodo.

        Retorna:
        bool: True si este nodo tiene un valor de f (f = g + h) menor que el otro nodo.
        """
        return (self.g + self.h) < (other.g + other.h)

def calculate_manhattan_distance(node, goal):
    """
    Calcula la distancia de Manhattan entre un nodo y el objetivo.

    Parámetros:
    node (Node): Nodo actual.
    goal (tuple): Coordenadas (fila, columna) del objetivo.

    Retorna:
    int: Distancia de Manhattan entre el nodo actual y el objetivo.
    """
    return abs(node.position[0] - goal[0]) + abs(node.position[1] - goal[1])

def astar(grid, start, goal):
    """
    Implementa el algoritmo A* para encontrar la ruta más corta entre dos puntos en una cuadrícula.

    Parámetros:
    grid (list): La cuadrícula representada como una lista de listas.
    start (tuple): Coordenadas (fila, columna) del punto de inicio.
    goal (tuple): Coordenadas (fila, columna) del punto de fin.

    Retorna:
    list: Lista de coordenadas que representan la ruta desde el punto de inicio hasta el punto de fin.
    """
    rows, cols = len(grid), len(grid[0])
    open_list = []  # Lista de nodos abiertos, ordenados por f = g + h
    visited = set()  # Conjunto de nodos visitados
    
    start_node = Node(start)  # Nodo de inicio
    start_node.g = start_node.h = 0  # Costo acumulado y heurística
    
    heapq.heappush(open_list, start_node)  # Agrega el nodo inicial a la lista de nodos abiertos
    
    while open_list:
        current_node = heapq.heappop(open_list)  # Obtiene el nodo con menor f
        
        if current_node.position == goal:
            # Reconstruye y devuelve la ruta
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
        
        visited.add(current_node.position)
        
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r, c = current_node.position[0] + dr, current_node.position[1] + dc
            
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1 and (r, c) not in visited:
                neighbor = Node((r, c), current_node)
                neighbor.g = current_node.g + 1  # Costo acumulado hasta el vecino
                neighbor.h = calculate_manhattan_distance(neighbor, goal)  # Heurística
                
                heapq.heappush(open_list, neighbor)  # Agrega el vecino a la lista de nodos abiertos
    
    return None

# Ejemplo de uso
grid = [[1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]]

start = (0, 0)
goal = (3, 4)

path = astar(grid, start, goal)

if path:
    print("Ruta encontrada:", path)
else:
    print("No se encontró una ruta.")
