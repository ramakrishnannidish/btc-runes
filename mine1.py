import subprocess

def mine_first_block(address):
    # Mine the first block
    subprocess.run(["bitcoin-cli", "-datadir=env", "generatetoaddress", "6", address])
