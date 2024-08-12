import heapq
from typing import Dict, List, Optional, Tuple

from helpers import Map

def heuristic(a: Tuple[float, float], b: Tuple[float, float]) -> float:
    """
    Calculate the Euclidean distance between two points.

    Args:
        a (Tuple[float, float]): The coordinates of the first point (x1, y1).
        b (Tuple[float, float]): The coordinates of the second point (x2, y2).

    Returns:
        float: The Euclidean distance between the two points.
    """
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def reconstruct_path(came_from: Dict[int, int], current: int) -> List[int]:
    """
    Reconstruct the path from the start node to the goal node.

    Args:
        came_from (Dict[int, int]): A dictionary mapping each node to the node it came from.
        current (int): The goal node.

    Returns:
        List[int]: The reconstructed path from the start node to the goal node.
    """
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]

def shortest_path(M: Map, start: int, goal: int) -> Optional[List[int]]:
    """
    Find the shortest path between two nodes in a map using the A* algorithm.

    Args:
        M (Map): The map containing the graph, intersections, and roads.
        start (int): The starting node.
        goal (int): The goal node.

    Returns:
        Optional[List[int]]: The shortest path from the start node to the goal node, or None if no path is found.
    """
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    came_from = {}
    
    g_score = {node: float('inf') for node in M.intersections}
    g_score[start] = 0
    
    f_score = {node: float('inf') for node in M.intersections}
    f_score[start] = heuristic(M.intersections[start], M.intersections[goal])
    
    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == goal:
            return reconstruct_path(came_from, current)
        
        for neighbor in M.roads[current]:
            tentative_g_score = g_score[current] + heuristic(M.intersections[current], M.intersections[neighbor])
            
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(M.intersections[neighbor], M.intersections[goal])
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None  # If there is no path