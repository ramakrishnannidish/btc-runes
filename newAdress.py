import subprocess
import json

def generate_regtest_address():
    result = subprocess.run(
        ["ord", "--data-dir", "env", "wallet", "receive"],
        capture_output=True,
        text=True
    )
    # Parse the JSON output
    address_info = json.loads(result.stdout)
    address = address_info['addresses'][0]
    return address

regtest_address = generate_regtest_address()
print(f"Generated regtest address: {regtest_address}")

def send_runes(receive_address, amount, rune_name):
    subprocess.run(
        ["ord", "--data-dir", "env", "wallet", "send", receive_address, f"{amount}:{rune_name}", "--fee-rate", "1"]
    )

def mine_block(address, number_of_blocks=1):
    subprocess.run(
        ["bitcoin-cli", "-datadir=env", "generatetoaddress", str(number_of_blocks), address]
    )

def check_wallet_balance():
    result = subprocess.run(
        ["ord", "--data-dir", "env", "wallet", "balance"],
        capture_output=True,
        text=True
    )
    balance = result.stdout.strip()
    return balance

# Run the workflow
regtest_address = generate_regtest_address()
print(f"Generated regtest address: {regtest_address}")

send_runes(regtest_address, "1000", "THE•DOG•RUNEKKKK")
mine_block(regtest_address)

wallet_balance = check_wallet_balance()
print(f"Wallet balance: {wallet_balance}")
