import os
from typing import Tuple
from algosdk import kmd, wallet, account

# LocalNet connections infos see: https://developer.algorand.org/docs/get-details/algokit/features/localnet/
# When creating resources, everything is based on the current config located in ~/.config/algokit

def get_account_filename(account_name):
    return f".{account_name}"

def load_account(name) -> Tuple[str, str] | None:
    filename = get_account_filename(name)
    if not os.path.exists(filename):
        return None
    with open(filename, "r") as f:
        private_key, address = f.read().splitlines()
    return private_key, address

def save_account(name, private_key, address):
    filename = get_account_filename(name)
    with open(filename, "w") as f:
        f.write(f"{private_key}\n{address}")

def generate_account(name) -> Tuple[str, str]:
    result = load_account(name)
    if result is not None:
        private_key, address = result
        return private_key, address
    private_key, address = account.generate_account()
    save_account(name, private_key, address)
    return private_key, address

wallets = ["admin", "emitter", "buyer"]

for wallet in wallets:
    admin_private_key, admin_address = generate_account(wallet)
    print(f"Created account: [{admin_private_key}] | [{admin_address}]")

# 1. Start localnet
# 2. Create necessary accounts
#   - app_admin
#   - emitter
#   - buyer_1
# 3. Deploy smart contract


