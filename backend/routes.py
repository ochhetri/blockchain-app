# backend/routes.py
from flask import Blueprint, jsonify, request
from .blockchain_utils import get_eth_balance, check_connection

# Create a Blueprint
main_bp = Blueprint('main', __name__)

@main_bp.route('/api/status', methods=['GET'])
def status():
    """API endpoint to check blockchain connection status."""
    connected = check_connection()
    return jsonify({
        "status": "connected" if connected else "disconnected",
        "message": "Blockchain node connection is active." if connected else "Failed to connect to blockchain node."
    })

@main_bp.route('/api/balance/<address>', methods=['GET'])
def get_balance_route(address):
    """API endpoint to get the balance of a specific address."""
    if not address:
        return jsonify({"error": "Address parameter is required"}), 400

    # Sanitize or validate address input if necessary (Web3.py does some validation)
    result = get_eth_balance(address)

    if "error" in result:
        # Determine appropriate status code based on error
        if "Invalid Ethereum address format" in result["error"]:
            status_code = 400 # Bad Request
        elif "node not connected" in result["error"]:
             status_code = 503 # Service Unavailable
        else:
             status_code = 500 # Internal Server Error
        return jsonify(result), status_code
    else:
        return jsonify(result), 200