import time
import random
from solana.rpc.api import Client
from wallet_manager import load_wallet, get_sol_balance
from serum_trading import place_market_order
from config import SOLANA_RPC_URL, WALLET_PRIVATE_KEY, MAX_TRADE_SIZE, STOP_LOSS_THRESHOLD

def run_trading_bot():
    # Initialize Solana client and wallet
    client = Client(SOLANA_RPC_URL)
    wallet = load_wallet(WALLET_PRIVATE_KEY)

    # Display initial wallet balance
    balance = get_sol_balance(wallet, client)
    print(f"Initial Balance: {balance} SOL")

    while True:
        # Fetch updated balance
        balance = get_sol_balance(wallet, client)
        print(f"Current Balance: {balance} SOL")

        # Randomly decide to buy or sell (for the purpose of this demo)
        action = random.choice(['buy', 'sell'])
        amount_to_trade = random.uniform(0.1, MAX_TRADE_SIZE)  # Random amount to trade

        # Trade logic (simplified)
        print(f"Attempting to {action} {amount_to_trade} SOL...")
        response = place_market_order(wallet, client, amount_to_trade, side=action)
        print(f"Trade Result: {response}")

        # Risk management: Stop loss
        if balance < STOP_LOSS_THRESHOLD * balance:
            print(f"Stop loss triggered, selling all...")
            place_market_order(wallet, client, balance, side='sell')

        # Sleep before next trade
        time.sleep(5)  # Adjust as needed

if __name__ == "__main__":
    run_trading_bot()
