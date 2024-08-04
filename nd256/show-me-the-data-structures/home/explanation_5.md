The `Blockchain` class is designed to simulate a simple blockchain, a data structure that maintains a growing list of records, called blocks, which are linked using cryptographic hashes. The class uses a list to store the chain of blocks, which is an efficient choice for maintaining the order of blocks and allowing easy access to the last block for appending new blocks. The `create_genesis_block` method initializes the chain with a genesis block, ensuring the blockchain starts with a valid block. The `add_block` method appends new blocks to the chain, linking them to the previous block via its hash, which maintains the integrity and immutability of the blockchain.

### Time Efficiency
- **Initialization (`__init__` method)**: $O(1)$ - Creating an empty list and adding the genesis block are constant-time operations.
- **Adding a Block (`add_block` method)**: $O(1)$ - Appending to the end of a list and accessing the last element are constant-time operations.
- **String Representation (`__repr__` method)**: $O(n)$ - Iterating through the list of blocks to create a string representation takes linear time relative to the number of blocks.

### Space Efficiency
- **Chain Storage**: $O(n)$ - The space required to store the blockchain grows linearly with the number of blocks.
- **Block Storage**: Each block stores its own data and the hash of the previous block, which adds a constant amount of space per block.

Overall, the `Blockchain` class is designed to be efficient in both time and space, leveraging the simplicity and performance characteristics of Python lists to manage the chain of blocks.