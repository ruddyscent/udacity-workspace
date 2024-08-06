from typing import Optional, Set

class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next: Optional[Node] = None

    def __repr__(self) -> str:
        return str(self.value)


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None

    def __str__(self) -> str:
        cur_head: Optional[Node] = self.head
        out_string: str = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string.strip(" -> ")

    def append(self, value: int) -> None:
        if self.head is None:
            self.head = Node(value)
            return

        node: Node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self) -> int:
        size: int = 0
        node: Optional[Node] = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    # Use a set to store all unique elements
    elements: Set[int] = set()

    current: Optional[Node] = llist_1.head
    while current:
        elements.add(current.value)
        current = current.next

    current = llist_2.head
    while current:
        elements.add(current.value)
        current = current.next

    # Create a new linked list to store the union
    union_list = LinkedList()
    for element in elements:
        union_list.append(element)

    return union_list

def intersection(llist_1: LinkedList, llist_2: LinkedList) -> LinkedList:
    # Use sets to find the intersection
    elements_1: Set[int] = set()
    elements_2: Set[int] = set()

    current: Optional[Node] = llist_1.head
    while current:
        elements_1.add(current.value)
        current = current.next

    current = llist_2.head
    while current:
        elements_2.add(current.value)
        current = current.next

    # Find the intersection of both sets
    common_elements: Set[int] = elements_1.intersection(elements_2)

    # Create a new linked list to store the intersection
    intersection_list = LinkedList()
    for element in common_elements:
        intersection_list.append(element)

    return intersection_list

if __name__ == "__main__":
    ## Test case 1
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
    
    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print("Test Case 1:")
    print("Union:", union(linked_list_1, linked_list_2)) # Expected: 1, 2, 3, 4, 6, 9, 11, 21, 32, 35, 65
    print("Intersection:", intersection(linked_list_1, linked_list_2)) # Expected: 4, 6, 21

    ## Test case 2
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print("\nTest Case 2:")
    print("Union:", union(linked_list_3, linked_list_4)) # Expected: 1, 2, 3, 4, 6, 7, 8, 9, 11, 21, 23, 35, 65
    print("Intersection:", intersection(linked_list_3, linked_list_4)) # Expected: empty

    ## Test case 3: Edge case with null or empty lists
    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    print("\nTest Case 3:")
    print("Union:", union(linked_list_5, linked_list_6))  # Expected: empty
    print("Intersection:", intersection(linked_list_5, linked_list_6))  # Expected: empty

    ## Test case 4: One list is empty
    linked_list_7 = LinkedList()
    linked_list_8 = LinkedList()

    element_1 = [1, 2, 3, 4, 5]
    for i in element_1:
        linked_list_7.append(i)

    print("\nTest Case 4:")
    print("Union:", union(linked_list_7, linked_list_8))  # Expected: 1, 2, 3, 4, 5
    print("Intersection:", intersection(linked_list_7, linked_list_8))  # Expected: empty

    ## Test case 5: Very large values
    linked_list_9 = LinkedList()
    linked_list_10 = LinkedList()

    element_1 = [10**10, 10**11, 10**12]
    element_2 = [10**12, 10**13, 10**14]

    for i in element_1:
        linked_list_9.append(i)

    for i in element_2:
        linked_list_10.append(i)

    print("\nTest Case 5:")
    print("Union:", union(linked_list_9, linked_list_10))  # Expected: 10**10, 10**11, 10**12, 10**13, 10**14
    print("Intersection:", intersection(linked_list_9, linked_list_10))  # Expected: 10**12
