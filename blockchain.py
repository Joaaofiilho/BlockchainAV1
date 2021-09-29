from block import Block

class BlockChain(object):

    def __init__(self):
        """
        chain: this variable stores all the blocks.
        current_data: this variable stores information about the transactions in the block.
        """
        self.chain = []
        self.build_genesis()

    def build_genesis(self):
        """creates the initial block in the chain, a block without any predecessors."""
        self.build_block(previous_hash=0)

    def build_block(self, previous_hash):

        block = Block(
        index=len(self.chain),
        previous_hash=previous_hash)

        self.chain.append(block)

        return block

    @staticmethod
    def confirm_validity(block, previous_block):
        """checks the integrity of the blockchain."""
        if previous_block.index + 1 != block.index:

            return False

        elif previous_block.hash != block.previous_hash:

            return False

        elif not block.verify(block.hash):

            return False

        return True

    @property
    def latest_block(self):
        """returns the last block of the network."""
        return self.chain[-1]

    def block_mining(self):

        last_block = self.latest_block
        last_hash = last_block.hash
        block = self.build_block(last_hash)

        while (not block.verify(block.hash)):
            block.nonce = block.nonce + 1
            block.hash = block.compute_hash()

        return vars(block)  

