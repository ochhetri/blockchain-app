# backend/app.py - Snippet
import os
# ... other imports
def create_app():
    app = Flask(__name__)
    # --- Configuration ---
    # Restrict CORS in production
    prod_origin = os.getenv('CORS_ORIGIN', '*') # Default to '*' if not set
    # Ensure it's a list if needed, or handle single origin string
    origins = [prod_origin] if prod_origin != '*' else '*'
    CORS(app, resources={r"/api/*": {"origins": origins}})
    # ... rest of the app factory
    return app