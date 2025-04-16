# backend/app.py
from flask import Flask
from flask_cors import CORS
from .routes import main_bp
import os

# --- Application Factory Function ---
def create_app():
    """Creates and configures the Flask application."""
    app = Flask(__name__)

    # --- Configuration ---
    # Enable CORS for requests from your frontend domain
    # In development, allow all origins, or specify your Vue dev server URL
    # In production, restrict this to your Netlify domain
    CORS(app, resources={r"/api/*": {"origins": "*"}}) # Allow all for now, restrict later
    # Example for production:
    # CORS(app, resources={r"/api/*": {"origins": "https://your-netlify-app-name.netlify.app"}})

    # Load environment variables (optional here as loaded in blockchain_utils, but good practice)
    # from dotenv import load_dotenv
    # load_dotenv()

    # --- Register Blueprints ---
    app.register_blueprint(main_bp)

    # --- Root Route (Optional - Simple health check) ---
    @app.route('/')
    def index():
        return "Blockchain API Backend is running!"

    return app

# --- Main Execution ---
# This block allows running the app directly using `python app.py` for local testing
# Gunicorn will call create_app() directly when deployed
if __name__ == '__main__':
    app = create_app()
    # Use host='0.0.0.0' to make it accessible on your network
    # Debug=True enables auto-reloading and detailed error pages (DO NOT use in production)
    port = int(os.environ.get("PORT", 5001)) # Use port 5001 for local dev
    app.run(host='0.0.0.0', port=port, debug=True)