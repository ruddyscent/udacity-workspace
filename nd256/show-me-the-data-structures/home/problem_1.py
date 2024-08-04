from collections import OrderedDict
from typing import Any, Optional

class LRU_Cache:
    def __init__(self, capacity: int) -> None:
        self.capacity: int = capacity
        self.cache: OrderedDict[int, Any] = OrderedDict()

    def get(self, key: int) -> Optional[Any]:
        if key not in self.cache:
            return -1
        else:
            # Move the accessed key to the end to mark it as recently used
            self.cache.move_to_end(key)
            return self.cache[key]

    def set(self, key: int, value: Any) -> None:
        if key in self.cache:
            # Update the value and mark the key as recently used
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            # Remove the first item in the ordered dictionary
            self.cache.popitem(last=False)

if __name__ == '__main__':
    # Testing the LRU_Cache class

    # Test Case 1: Basic functionality
    our_cache = LRU_Cache(5)
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    assert our_cache.get(1) == 1   # Returns 1
    assert our_cache.get(2) == 2   # Returns 2
    assert our_cache.get(9) == -1  # Returns -1 because 9 is not in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)  # This should evict key 3
    assert our_cache.get(3) == -1  # Returns -1, 3 was evicted

    # Test Case 2: Edge case with very large numbers
    large_cache = LRU_Cache(2)
    large_cache.set(10**9, 10**9)
    large_cache.set(10**10, 10**10)
    assert large_cache.get(10**9) == 10**9  # Returns 10**9
    large_cache.set(10**11, 10**11)         # This should evict key 10**10
    assert large_cache.get(10**10) == -1    # Returns -1
    assert large_cache.get(10**11) == 10**11  # Returns 10**11

    # Test Case 3: Edge case with null/empty values
    null_cache = LRU_Cache(2)
    null_cache.set(0, None)
    null_cache.set(1, "")
    assert null_cache.get(0) is None  # Returns None
    assert null_cache.get(1) == ""    # Returns empty string