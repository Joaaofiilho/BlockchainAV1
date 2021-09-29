import time
import hashlib


class Block(object):

    def __init__(self, index, previous_hash, timestamp=None):
        """
        index: it’s used to track the position of a block within the blockchain.
        previous_hash: it used to reference the hash of the previous block within the blockchain.
        data: it gives details of the transactions done, for example, the amount bought.
        timestamp: it inserts a timestamp for all the transactions performed.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp or time.time()
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        """it is used to produce the cryptographic hash of each block based on the index, proof_number, previous_hash and data values."""
        string_block = "{}{}{}{}".format(
            self.index, self.nonce, self.previous_hash, self.timestamp)

        return hashlib.sha256(string_block.encode()).hexdigest()

    def verify(self, hash):
        difficulty = 3
        number_of_zeros = 0
        for i in range(difficulty):
            if hash[i] == "0":
                number_of_zeros = number_of_zeros + 1

        return number_of_zeros == difficulty

    def __repr__(self):
        return "\nBlock: index: {},\nnonce: {},\nhash: {},\nprevious_hash: {},\ntimestamp: {}".format(self.index, self.nonce, self.hash, self.previous_hash, self.timestamp)
