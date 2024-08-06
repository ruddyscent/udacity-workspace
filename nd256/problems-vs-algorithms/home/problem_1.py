def sqrt(number: int) -> int:
    """
    Calculate the floored square root of a number

    Args:
    number(int): Number to find the floored square root

    Returns:
    int: Floored Square Root
    """
    if number < 0:
        return None  # Square root is not defined for negative numbers
    if number == 0 or number == 1:
        return number  # Square root of 0 is 0, square root of 1 is 1
    
    low, high = 1, number // 2
    result: int = 0  # Initialize result with a default value
    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid
        if mid_squared == number:
            return mid
        elif mid_squared < number:
            low = mid + 1
            result = mid  # Keep track of the last valid result
        else:
            high = mid - 1
    
    return result  # Return the largest `mid` such that `mid * mid` is <= number

if __name__ == "__main__":
    # Test cases
    print("Pass" if 3 == sqrt(9) else "Fail")   # Expected Output: Pass
    print("Pass" if 0 == sqrt(0) else "Fail")   # Expected Output: Pass
    print("Pass" if 4 == sqrt(16) else "Fail")  # Expected Output: Pass
    print("Pass" if 1 == sqrt(1) else "Fail")   # Expected Output: Pass
    print("Pass" if 5 == sqrt(27) else "Fail")  # Expected Output: Pass