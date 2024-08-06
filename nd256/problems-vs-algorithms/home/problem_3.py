from typing import List, Tuple

def rearrange_digits(input_list: List[int]) -> Tuple[int, int]:
    # Custom quicksort implementation
    def quicksort(arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x > pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x < pivot]
        return quicksort(left) + middle + quicksort(right)

    # Sort the array in descending order
    sorted_list = quicksort(input_list)

    # Form two numbers by alternating the digits
    num1: int = 0
    num2: int = 0
    for i, value in enumerate(sorted_list):
        if i % 2 == 0:
            num1 = num1 * 10 + value
        else:
            num2 = num2 * 10 + value

    return num1, num2

def test_function(test_case: Tuple[List[int], List[int]]) -> None:
    output: Tuple[int, int] = rearrange_digits(test_case[0])
    solution: List[int] = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

if __name__ == '__main__':
    # Edge case: Single element list
    test_function(([9], [9, 0]))
    # Expected output: Pass

    # Edge case: Large input list
    test_function(([i for i in range(1000, 0, -1)], [int(''.join(map(str, range(999, 0, -2)))), int(''.join(map(str, range(998, 0, -2))))]))
    # Expected output: Pass

    # Edge case: List with negative numbers
    test_function(([-1, -2, -3, -4, -5], [-135, -24]))
    # Expected output: Pass

    # Normal case: Mixed positive and negative numbers
    test_function(([3, -2, 1, -4, 5], [531, -42]))
    # Expected output: Pass

    # Normal case: List with zeros
    test_function(([0, 0, 0, 0, 0], [0, 0]))
    # Expected output: Pass

    # Normal case: List with repeated numbers
    test_function(([2, 2, 2, 2, 2], [222, 2]))
    # Expected output: Pass