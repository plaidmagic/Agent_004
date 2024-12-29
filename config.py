import os
from dotenv import load_dotenv

load_dotenv()

# Solana Wallet Configuration
WALLET_PRIVATE_KEY = os.getenv("WALLET_PRIVATE_KEY")

# Solana Client URL
SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"

# Serum DEX API Endpoint
SERUM_API_URL = "https://serum-api.bonfida.com"

# Risk Management
MAX_TRADE_SIZE = 10  # Max SOL to trade per transaction
STOP_LOSS_THRESHOLD = 0.95  # 5% stop-loss
