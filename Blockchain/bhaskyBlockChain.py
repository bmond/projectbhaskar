import bhaskyCoin 
import bhaskyGenesisBlock
import bhaskyNewBlock
# Create the blockchain and add the genesis block
blockchain = [bhaskyGenesisBlock.create_genesis_block()]
previous_block = blockchain[0]
print "just checking"

# How many blocks should we add to the chain
# after the genesis block
num_of_blocks_to_add = 20

# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
  block_to_add = bhaskyNewBlock.next_block(previous_block)
  blockchain.append(block_to_add)
  previous_block = block_to_add
  # Tell everyone about it!
  print "Block #{} has been added to the blockchain!".format(block_to_add.index)
  print "Hash: {}\n".format(block_to_add.hash) 
