import os
from typing import Tuple
from algosdk import kmd, mnemonic, name, account
import argparse

import algosdk
from algosdk.v2client import algod

# LocalNet connections infos see: https://developer.algorand.org/docs/get-details/algokit/features/localnet/
# When creating resources, everything is based on the current config located in ~/.config/algokit

def get_account_filename(account_name):
    return f".{account_name}"

def load_account(name) -> Tuple[str, str, str] | None:
    filename = get_account_filename(name)
    if not os.path.exists(filename):
        return None
    with open(filename, "r") as f:
        private_key, address = f.read().splitlines()
    return private_key, address, mnemonic.from_private_key(private_key)

def save_account(name, private_key, address):
    filename = get_account_filename(name)
    with open(filename, "w") as f:
        f.write(f"{private_key}\n{address}")

def generate_account(name) -> Tuple[str, str, str]:
    result = load_account(name)
    if result is not None:
        private_key, address, passphrase = result
        return private_key, address, passphrase
    private_key, address = account.generate_account()
    save_account(name, private_key, address)
    return private_key, address, mnemonic.from_private_key(private_key)

#
# 1. Start localnet
# 2. Create necessary accounts
#   - app_admin
#   - emitter
#   - buyer_1
# 3. Deploy smart contract


parser = argparse.ArgumentParser(prog="bootstrap", description="Bootstrap paypay algorand dependencies")
parser.add_argument("--reset", action="store_true")

args = parser.parse_args()

wallets = {
    "admin": {},
    "emitter": {},
    "buyer": {}
}

if args.reset:
    for name in wallets:
        filename = get_account_filename(name)
        if os.path.exists(filename):
            print(f"deleting {filename}")
            os.remove(filename)



algod_address = "http://localhost:4001"
algod_token = "a" * 64

algod_client = algod.AlgodClient(algod_token, algod_address)

for name in wallets.keys():
    private_key, address, passphrase = generate_account(name)
    wallets[name] = {
        "private_key": private_key,
        "address": address,
        "passphrase": passphrase,
    }
    print(f"Created account: \n\t private key: {private_key} \n\tAddress: {address} \n\tPassphrase: {passphrase}")
    print()


account_info = algod_client.account_info(wallets["admin"]["address"])
print(account_info)
