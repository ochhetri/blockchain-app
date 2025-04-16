# backend/blockchain_utils.py
import os
from web3 import Web3
from web3.exceptions import InvalidAddress
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

# Initialize Web3
# Use the RPC URL from the environment variables
rpc_url = os.getenv("SEPOLIA_RPC_URL", "https://rpc.sepolia.org/") # Provide a default fallback
if not rpc_url:
    raise ValueError("SEPOLIA_RPC_URL not found in environment variables.")

try:
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    # Check connection (optional but good practice)
    if not w3.is_connected():
        print(f"Warning: Failed to connect to Web3 provider at {rpc_url}")
        # Handle connection failure appropriately if needed
except Exception as e:
    print(f"Error initializing Web3: {e}")
    # Optionally, raise the exception or handle it
    w3 = None # Indicate that Web3 is not available

def check_connection():
    """Checks if Web3 is connected to the node."""
    if w3:
        return w3.is_connected()
    return False

def get_eth_balance(address: str) -> dict:
    """
    Retrieves the Ether balance for a given address on the Sepolia network.

    Args:
        address: The Ethereum address (hex string).

    Returns:
        A dictionary containing the address, balance in Ether,
        balance in Wei, or an error message.
    """
    if not w3 or not check_connection():
        return {"error": "Blockchain node not connected"}

    try:
        # Validate the address format before checking balance
        checksum_address = w3.to_checksum_address(address)
        balance_wei = w3.eth.get_balance(checksum_address)
        balance_ether = w3.from_wei(balance_wei, 'ether')
        return {
            "address": checksum_address,
            "balance_wei": str(balance_wei), # Return as string for precision
            "balance_ether": str(balance_ether)
        }
    except InvalidAddress:
        return {"error": f"Invalid Ethereum address format: {address}"}
    except Exception as e:
        # Catch potential network errors or other issues
        print(f"Error retrieving balance for {address}: {e}")
        return {"error": f"Could not retrieve balance. Check node connection or address."}