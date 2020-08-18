import bhaskyCoin
import datetime as date

def create_genesis_block():
  # Manually construct a block with
  # index zero and arbitrary previous hash
  return bhaskyCoin.Block(0, date.datetime.now(), "Genesis Block", "0")
