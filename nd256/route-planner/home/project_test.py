from helpers import load_map
from typing import Callable, List, Tuple

MAP_40_ANSWERS: List[Tuple[int, int, List[int]]] = [
    (5, 34, [5, 16, 37, 12, 34]),
    (5, 5,  [5]),
    (8, 24, [8, 14, 16, 37, 12, 17, 10, 24])
]

def test(shortest_path_function: Callable[[Map, int, int], List[int]]) -> None:
    """
    Test the shortest_path_function with predefined test cases.

    Args:
        shortest_path_function (Callable[[Map, int, int], List[int]]): 
            A function that takes a Map object, a start node, and a goal node, 
            and returns a list of nodes representing the shortest path.

    Returns:
        None
    """
    map_40 = load_map('map-40.pickle')
    correct = 0
    for start, goal, answer_path in MAP_40_ANSWERS:
        path = shortest_path_function(map_40, start, goal)
        if path == answer_path:
            correct += 1
        else:
            print("For start:", start, 
                  "Goal:     ", goal,
                  "Your path:", path,
                  "Correct:  ", answer_path)
    if correct == len(MAP_40_ANSWERS):
        print("All tests pass! Congratulations!")
    else:
        print("You passed", correct, "/", len(MAP_40_ANSWERS), "test cases")
    