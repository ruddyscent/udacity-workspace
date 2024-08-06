from typing import List, Tuple, Optional

def get_min_max(ints: List[int]) -> Optional[Tuple[int, int]]:
    """
    Return a tuple(min, max) out of list of unsorted integers.
    
    Args:
    ints (List[int]): list of integers containing one or more integers

    Returns:
    Optional[Tuple[int, int]]: A tuple containing the minimum and maximum integer, or None if the list is empty
    """
    if not ints:
        return None  # Returning None if the list is empty
    
    # Initialize min and max to the first element of the list
    minimum = maximum = ints[0]
    
    # Iterate through the list, updating min and max
    for number in ints:
        if number > maximum:
            maximum = number
        elif number < minimum:
            minimum = number
    
    return (minimum, maximum)

if __name__ == '__main__':
    # Edge case: Empty input list
    print(get_min_max([]))
    # Expected output: None

    # Edge case: List with one element
    print(get_min_max([42]))
    # Expected output: (42, 42)

    # Edge case: List with all identical elements
    print(get_min_max([7, 7, 7, 7, 7]))
    # Expected output: (7, 7)

    # Normal case: List with negative and positive numbers
    print(get_min_max([-10, 0, 10, -20, 20]))
    # Expected output: (-20, 20)

    # Normal case: List with large range of numbers
    print(get_min_max([1000, -1000, 500, -500, 0]))
    # Expected output: (-1000, 1000)

    # Normal case: List with already sorted numbers
    print(get_min_max([1, 2, 3, 4, 5]))
    # Expected output: (1, 5)