import heapq
from collections import defaultdict
from typing import Dict, Optional, Tuple

# Huffman Tree Node
class HuffmanNode:
    def __init__(self, char: Optional[str], freq: int) -> None:
        self.char: Optional[str] = char
        self.freq: int = freq
        self.left: Optional[HuffmanNode] = None
        self.right: Optional[HuffmanNode] = None

    def __lt__(self, other: 'HuffmanNode') -> bool:
        return self.freq < other.freq

def calculate_frequencies(data: str) -> Dict[str, int]:
    frequency: Dict[str, int] = defaultdict(int)
    for char in data:
        frequency[char] += 1
    return frequency

def build_huffman_tree(frequency: Dict[str, int]) -> HuffmanNode:
    priority_queue: List[HuffmanNode] = []
    for char, freq in frequency.items():
        node = HuffmanNode(char, freq)
        heapq.heappush(priority_queue, node)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return heapq.heappop(priority_queue)

def generate_huffman_codes(node: Optional[HuffmanNode], code: str, huffman_codes: Dict[str, str]) -> None:
    if node is None:
        return

    if node.char is not None:
        huffman_codes[node.char] = code
        return

    generate_huffman_codes(node.left, code + "0", huffman_codes)
    generate_huffman_codes(node.right, code + "1", huffman_codes)

def huffman_encoding(data: str) -> Tuple[str, Optional[HuffmanNode]]:
    if not data:
        return "", None

    frequency = calculate_frequencies(data)
    root = build_huffman_tree(frequency)

    huffman_codes: Dict[str, str] = {}
    generate_huffman_codes(root, "", huffman_codes)

    # Handle the case where the input consists of a single unique character
    if len(huffman_codes) == 1:
        # Assign '0' as the encoding for the single character
        single_char = next(iter(huffman_codes))
        huffman_codes[single_char] = '0'

    encoded_data = ''.join(huffman_codes[char] for char in data)
    return encoded_data, root

def huffman_decoding(encoded_data: str, tree: Optional[HuffmanNode]) -> str:
    if not tree or not encoded_data:
        return ""

    # Handle the case where the tree consists of a single node (single character)
    if tree.left is None and tree.right is None:
        # Return the repeated single character
        return tree.char * len(encoded_data)

    decoded_data = []
    current_node = tree

    for bit in encoded_data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.left is None and current_node.right is None:
            decoded_data.append(current_node.char)
            current_node = tree

    return ''.join(decoded_data)

# Main Function
if __name__ == "__main__":
    # Test Case 1: Standard test case
    print("\nTest Case 1: Standard sentence")
    sentence = "Huffman coding is fun!"
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert sentence == decoded_data

    # Test Case 2: Edge case with a single character repeated
    print("\nTest Case 2: Single repeated character")
    sentence = "aaaaaa"
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert sentence == decoded_data

    # Test Case 3: Edge case with empty string
    print("\nTest Case 3: Empty string")
    sentence = ""
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert sentence == decoded_data

    # Test Case 4: Edge case with a very large string
    print("\nTest Case 4: Very large string")
    sentence = "ab" * 10000
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded data size:", len(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    assert sentence == decoded_data
