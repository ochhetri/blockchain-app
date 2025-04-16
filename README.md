# Sepolia ETH Balance Checker


## Overview

A simple web application built to check the Ether (ETH) balance of any wallet address on the Ethereum Sepolia test network. This project serves as a demonstration of integrating a Python Flask backend (using Web3.py) with a Vue.js frontend to interact with blockchain data. The backend provides an API, and the frontend consumes it to display information to the user.

The application is deployed with the backend on Render and the frontend on Netlify, utilizing their free tiers.

## Live Demo

🚀 **Try the live application here:** [https://blockchain-tracker.netlify.app/](https://blockchain-tracker.netlify.app/)

*(Note: The backend might take ~30 seconds to wake up on the first request due to Render's free tier scaling.)*

## Screenshot

![Blockchain Balance Checker Screenshot](/frontend/public/img/screenshot.png)


## Features Implemented

*   **Wallet Balance Check:** Input any Sepolia-compatible wallet address to view its ETH balance.
*   **Flask Backend API:** A Python API using Flask to handle requests.
*   **Web3.py Integration:** Connects to the Sepolia testnet via an RPC URL to fetch blockchain data.
*   **API Endpoints:** Provides endpoints for checking service status and fetching wallet balances.
*   **Vue.js Frontend:** A modern, responsive user interface built with Vue 3 and Vue Router.
*   **Tailwind CSS:** Utility-first CSS framework for styling.
*   **Axios:** Used for making HTTP requests from the frontend to the backend API.
*   **Responsive Design:** Adapts to different screen sizes (desktop, tablet, mobile).
*   **Deployment:** Backend deployed on Render, Frontend deployed on Netlify.

## Tech Stack

*   **Frontend:**
    *   Vue.js (v3)
    *   Vue Router
    *   Tailwind CSS
    *   Axios
    *   (Future: Ethers.js/Web3.js for MetaMask)
    *   (Future: vue-qrcode-component)
*   **Backend:**
    *   Python 3.11+
    *   Flask
    *   Flask-CORS
    *   Web3.py
    *   Gunicorn (for deployment)
    *   python-dotenv
*   **Blockchain:**
    *   Ethereum Sepolia Testnet
    *   Public RPC Node (e.g., Alchemy, Infura, or public endpoints)
    *   (Future: SimpleStorage Solidity Smart Contract)
*   **Deployment:**
    *   Backend: Render (Web Service - Free Tier)
    *   Frontend: Netlify (Static Site Hosting - Free Tier)
*   **Development:**
    *   Node.js / npm
    *   VS Code (Recommended)
    *   Git / GitHub

## Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

*   Git ([https://git-scm.com/](https://git-scm.com/))
*   Python 3.11+ and Pip ([https://www.python.org/](https://www.python.org/))
*   Node.js (LTS version recommended) and npm ([https://nodejs.org/](https://nodejs.org/))
*   A Sepolia RPC URL (e.g., from Alchemy, Infura, or a public provider)
*   (Optional) MetaMask browser extension for future features ([https://metamask.io/](https://metamask.io/))

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Garbii1/blockchain-app.git
    cd blockchain-app
    ```

2.  **Backend Setup:**
    *   Navigate to the backend directory:
        ```bash
        cd backend
        ```
    *   Create and activate a virtual environment:
        ```bash
        # Create
        python -m venv venv
        # Activate (Windows CMD/Git Bash)
        .\venv\Scripts\activate
        # Activate (macOS/Linux/WSL)
        # source venv/bin/activate
        ```
    *   Install Python dependencies:
        ```bash
        pip install -r requirements.txt
        ```
    *   Create a `.env` file in the `backend` directory:
        ```dotenv
        # backend/.env
        # Replace with your actual Sepolia RPC URL
        SEPOLIA_RPC_URL=https://rpc.sepolia.org/
        # Add these lines later if implementing contract interaction
        # CONTRACT_ADDRESS=YOUR_DEPLOYED_CONTRACT_ADDRESS
        # CONTRACT_ABI='YOUR_CONTRACT_ABI_JSON_STRING'
        ```

3.  **Frontend Setup:**
    *   Navigate to the frontend directory:
        ```bash
        # From project root
        cd ../frontend
        # Or from backend directory
        # cd ../frontend
        ```
    *   Install Node.js dependencies:
        ```bash
        npm install
        ```
    *   Create environment files for API URLs:
        *   Create `.env.development` in the `frontend` directory:
            ```dotenv
            # frontend/.env.development
            VUE_APP_API_BASE_URL=http://127.0.0.1:5001/api
            ```
        *   Create `.env.production` in the `frontend` directory (used for the deployed version):
            ```dotenv
            # frontend/.env.production
            # Replace with your *deployed* Render backend URL
            VUE_APP_API_BASE_URL=https://blockchain-app-s4fw.onrender.com/api
            ```
    *   *Ensure you created the `vue.config.js` file as per the troubleshooting steps to disable CSS url() processing if you encountered that issue.*

### Running Locally

1.  **Run the Backend (Flask):**
    *   Open a terminal in the **project root** (`blockchain-app/`).
    *   Activate the backend virtual environment:
        ```bash
        # Windows CMD/Git Bash
        .\backend\venv\Scripts\activate
        # macOS/Linux/WSL
        # source backend/venv/bin/activate
        ```
    *   Set Flask environment variables (use `set` for Windows CMD, `$env:` for PowerShell, `export` for macOS/Linux):
        ```bash
        # Example for Windows CMD (Run from project root!)
        set FLASK_APP=backend.app:create_app
        set FLASK_ENV=development
        # Example for macOS/Linux/WSL
        # export FLASK_APP=backend.app:create_app
        # export FLASK_ENV=development
        ```
    *   Run the Flask development server:
        ```bash
        flask run --port=5001
        ```
    *   The backend should now be running at `http://127.0.0.1:5001`. Keep this terminal open.

2.  **Run the Frontend (Vue):**
    *   Open a **new** terminal in the `frontend` directory (`blockchain-app/frontend/`).
    *   Run the Vue development server:
        ```bash
        npm run serve
        ```
    *   The frontend should now be running, typically at `http://localhost:8080` (check the terminal output). Open this URL in your browser.

## API Endpoints Overview

*   `GET /api/status`: Checks the connection status to the blockchain node.
*   `GET /api/balance/<address>`: Retrieves the ETH balance for the specified `<address>` on Sepolia.
*   `(Future) GET /api/contract/value`: Retrieves a stored value from a deployed smart contract.
*   `(Future) POST /api/contract/value`: Sets a value in a deployed smart contract (requires backend signing - complex).

## Deployment Notes

*   **Backend (Render):**
    *   Connect GitHub repo.
    *   **Root Directory:** `backend`
    *   **Build Command:** `pip install -r requirements.txt`
    *   **Start Command:** `gunicorn "backend.app:create_app()"` (Ensure quotes and parentheses are correct!)
    *   **Environment Variables:**
        *   `PYTHONPATH` = `/opt/render/project/src`
        *   `SEPOLIA_RPC_URL` = Your Sepolia RPC URL
        *   (Future: `CONTRACT_ADDRESS`, `CONTRACT_ABI`)
*   **Frontend (Netlify):**
    *   Connect GitHub repo.
    *   **Base directory:** `frontend`
    *   **Build command:** `npm run build`
    *   **Publish directory:** `frontend/dist`
    *   Ensure `frontend/public/_redirects` file exists with `/* /index.html 200` for Vue Router history mode.
    *   Ensure `.env.production` has the correct deployed Render API URL.

## Challenges Faced & Solutions

*   **Backend Relative Imports:** `ImportError: attempted relative import with no known parent package` when running Flask/Gunicorn.
    *   **Solution:** Run `flask run` or `gunicorn` commands with the app specified relative to the project root (e.g., `backend.app:create_app`) and set the `PYTHONPATH` environment variable on Render to `/opt/render/project/src`.
*   **Gunicorn Start Command:** Syntax errors or TypeErrors when using the factory pattern (`create_app`).
    *   **Solution:** Use the format `gunicorn "backend.app:create_app()"` ensuring quotes for the shell and parentheses for Gunicorn's factory detection.
*   **`pywin32` Dependency:** Build failure on Render (Linux) due to Windows-specific dependency.
    *   **Solution:** Remove `pywin32` from `backend/requirements.txt`.
*   **Frontend CSS Image Paths:** `Module not found: Error: Can't resolve '/img/...'` despite image existing in `public/img`. `css-loader` was resolving relative to the CSS file instead of the public root.
    *   **Solution (Workaround):** Disable URL processing in `css-loader` via `vue.config.js` by setting `chainWebpack` config to modify the loader's options: `options.url = false;`. This passes the root-relative URL directly to the browser.
*   **Frontend API URL:** Deployed frontend calling local backend URL.
    *   **Solution:** Ensure `VUE_APP_API_BASE_URL` in `frontend/.env.production` is correctly set to the deployed Render backend URL and that this file is committed before deploying to Netlify.
*   **Backend 503 Errors:** Deployed backend intermittently unavailable.
    *   **Solution:** Check Render logs for crashes/restarts. Verify RPC connection via `/api/status`. Understand free tier limitations (sleep/wake cycles, resource limits).

## Future Improvements

*   **MetaMask Integration:** Implement "Connect Wallet" functionality using `window.ethereum`.
*   **Smart Contract Interaction:**
    *   Deploy `SimpleStorage.sol` contract.
    *   Implement backend endpoint (`GET /api/contract/value`) to read from the contract.
    *   Implement frontend UI to display and refresh the contract value.
    *   (Advanced) Implement secure method for `setValue` (likely requires frontend signing via MetaMask/Ethers.js).
*   **QR Code Display:** Add QR code generation for displayed wallet addresses.
*   **Decentralized Marketplace:** Expand functionality towards a simple marketplace concept.
*   **Enhanced Error Handling:** More specific and user-friendly error messages on both frontend and backend.
*   **Loading Indicators:** More granular loading states for different operations.
*   **Unit & Integration Tests:** Add tests for backend and frontend components.
*   **Security Hardening:** Implement stricter CORS, input validation, and potentially rate limiting on the API.
*   **State Management (Frontend):** Use Pinia or Vuex for more complex state sharing if the app grows.

## Author

*   **Muhammed Babatunde Garuba**
*   GitHub: [@Garbii1](https://github.com/Garbii1)

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 