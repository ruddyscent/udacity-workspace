import hashlib
import datetime
from typing import List

class Block:
    def __init__(self, timestamp: datetime.datetime, data: str, previous_hash: str) -> None:
        self.timestamp: datetime.datetime = timestamp
        self.data: str = data
        self.previous_hash: str = previous_hash
        self.hash: str = self.calc_hash()

    def calc_hash(self) -> str:
        sha = hashlib.sha256()
        hash_str = (str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __repr__(self) -> str:
        return (f"Block(\n"
                f"  Timestamp: {self.timestamp},\n"
                f"  Data: {self.data},\n"
                f"  Previous Hash: {self.previous_hash},\n"
                f"  Hash: {self.hash}\n"
                f")\n")

class Blockchain:
    def __init__(self) -> None:
        self.chain: List[Block] = []
        self.create_genesis_block()

    def create_genesis_block(self) -> None:
        # Genesis block has no previous hash and empty data
        genesis_block = Block(datetime.datetime.utcnow(), "Genesis Block", "0")
        self.chain.append(genesis_block)

    def add_block(self, data: str) -> None:
        previous_block = self.chain[-1]
        new_block = Block(datetime.datetime.utcnow(), data, previous_block.hash)
        self.chain.append(new_block)

    def __repr__(self) -> str:
        chain_str = ""
        for block in self.chain:
            chain_str += str(block) + "\n"
        return chain_str

if __name__ == "__main__":
    # Test cases
    # Test Case 1: Create a blockchain and add blocks
    print("Test Case 1: Basic blockchain functionality")
    blockchain = Blockchain()
    blockchain.add_block("Block 1 Data")
    blockchain.add_block("Block 2 Data")
    blockchain.add_block("Block 3 Data")
    print(blockchain)

    # Test Case 2: Edge case with empty string as data
    print("Test Case 2: Add block with empty string data")
    blockchain = Blockchain()
    blockchain.add_block("")
    print(blockchain)

    # Test Case 3: Large data input
    print("Test Case 3: Add block with large data")
    large_data = "x" * 10000  # Large data string
    blockchain = Blockchain()
    blockchain.add_block(large_data)
    print(blockchain)

    # Test Case 4: Null data (None)
    print("Test Case 4: Add block with null data")
    blockchain = Blockchain()
    blockchain.add_block(None)  # Assuming we treat None as a string "None"
    print(blockchain)
