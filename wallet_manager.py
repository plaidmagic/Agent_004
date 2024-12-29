from solana.wallet import Wallet
from solana.rpc.api import Client
from solana.keypair import Keypair
import base64

def load_wallet(private_key_str):
    private_key = base64.b64decode(private_key_str)
    keypair = Keypair.from_secret_key(private_key)
    return Wallet(keypair)

def get_sol_balance(wallet: Wallet, client: Client):
    balance = client.get_balance(wallet.public_key())
    return balance['result']['value'] / 1e9  # Convert lamports to SOL

def sign_transaction(transaction, wallet: Wallet):
    return wallet.sign_transaction(transaction)
