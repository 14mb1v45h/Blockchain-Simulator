import hashlib
from datetime import datetime

class Block:
    def __init__(self, index, previous_hash, data):
        self.index = index
        self.timestamp = datetime.now()
        self.previous_hash = previous_hash
        self.data = data
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256(f"{self.index}{self.timestamp}{self.previous_hash}{self.data}{self.nonce}".encode()).hexdigest()

    def mine(self, difficulty):
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def add_block(self, data):
        previous_hash = self.chain[-1].hash
        new_block = Block(len(self.chain), previous_hash, data)
        new_block.mine(self.difficulty)
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            if self.chain[i].hash != self.chain[i].calculate_hash() or self.chain[i].previous_hash != self.chain[i-1].hash:
                return False
        return True

if __name__ == "__main__":
    bc = Blockchain()
    bc.add_block("Transaction 1")
    bc.add_block("Transaction 2")
    print("Blockchain valid?", bc.is_valid())
    for block in bc.chain:
        print(f"Block {block.index}: {block.data} ({block.hash})")