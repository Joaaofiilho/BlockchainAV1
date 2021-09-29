from blockchain import BlockChain

blockchain = BlockChain()

print("Iniciando mineração!")

# print(blockchain.chain)

for _ in range(5):
    blockchain.block_mining()

print("Mineração bem sucedida! Cadeia final:")

print(blockchain.chain)

def verify_blockchain(blockchain: BlockChain):
    chain = blockchain.chain

    for i in range(len(chain)):
        if i > 0:
            block = chain[i]
            previous_block = chain[i-1]
            if not blockchain.confirm_validity(block, previous_block):
                return False
    
    return True

print("Is the blockchain valid: {}".format(verify_blockchain(blockchain)))