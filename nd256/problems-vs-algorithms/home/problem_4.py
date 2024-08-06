from typing import List

def sort_012(input_list: List[int]) -> List[int]:
    low, mid, high = 0, 0, len(input_list) - 1
    
    while mid <= high:
        if input_list[mid] == 0:
            input_list[low], input_list[mid] = input_list[mid], input_list[low]
            low += 1
            mid += 1
        elif input_list[mid] == 1:
            mid += 1
        else:  # input_list[mid] == 2
            input_list[mid], input_list[high] = input_list[high], input_list[mid]
            high -= 1

    return input_list

def test_function(test_case: List[List[int]]) -> None:
    sorted_array: List[int] = sort_012(test_case[0])
    print(sorted_array)
    if sorted_array == sorted(test_case[0]):
        print("Pass")
    else:
        print("Fail")

if __name__ == "__main__":
    # Edge case: Empty input list
    test_function([[]])
    # Expected output: Pass

    # Edge case: Large input list
    test_function([[0, 1, 2] * 100000])
    # Expected output: Pass

    # Edge case: List with only one type of element
    test_function([[2, 2, 2, 2, 2]])
    # Expected output: Pass

    # Normal case: Mixed elements
    test_function([[0, 1, 2, 0, 1, 2]])
    # Expected output: Pass

    # Normal case: Already sorted list
    test_function([[0, 0, 1, 1, 2, 2]])
    # Expected output: Pass

    # Normal case: Reverse sorted list
    test_function([[2, 2, 1, 1, 0, 0]])
    # Expected output: Pass