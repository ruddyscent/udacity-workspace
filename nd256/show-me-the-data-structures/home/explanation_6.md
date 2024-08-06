The `union` and `intersection` functions are designed to operate on two sets, returning their union and intersection, respectively. These functions utilize Python's built-in set data structure, which is highly efficient for these types of operations due to its underlying implementation using hash tables.

### Union Function
The `union` function combines all unique elements from both sets into a new set. The decision to use the set data structure is driven by its $O(1)$ average time complexity for insertions and lookups, making the union operation efficient. The function leverages the `|` operator or the `union` method, both of which are optimized for set operations.

- **Time Efficiency**: $O(n + m)$, where n and m are the sizes of the two sets. This is because each element from both sets is processed once.
- **Space Efficiency**: $O(n + m)$, as a new set is created to store the combined elements from both sets.

### Intersection Function
The `intersection` function finds common elements between the two sets, returning a new set containing these elements. Using the set data structure is ideal here due to its efficient membership testing. The function uses the `&` operator or the `intersection` method, which are optimized for finding common elements between sets.

- **Time Efficiency**: $O(\min(n, m))$, where n and m are the sizes of the two sets. This is because the function iterates over the smaller set and checks membership in the larger set.
- **Space Efficiency**: $O(\min(n, m))$, as a new set is created to store the common elements, which will be at most the size of the smaller set.

Overall, the use of sets ensures that both the `union` and `intersection` functions are efficient in terms of both time and space, leveraging the properties of hash tables to perform these operations quickly.