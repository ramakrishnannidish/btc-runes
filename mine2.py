import subprocess

def mine_second_block(address):
    # Mine the second block
    subprocess.run(["bitcoin-cli", "-datadir=env", "generatetoaddress", "1", address])
