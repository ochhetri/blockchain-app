# 🌐 Blockchain App: Check Your ETH Balances on Sepolia Testnet

![Blockchain App](https://img.shields.io/badge/Check%20ETH%20Balances-Here-blue?style=for-the-badge&logo=ethereum)

Welcome to the **Blockchain App**! This simple web application allows you to check your Ethereum (ETH) balances on the Sepolia testnet. Built with a Flask backend and a Vue.js frontend, this app provides a seamless experience for users interested in exploring the world of blockchain and cryptocurrency.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Releases](#releases)
- [Contact](#contact)

## Features

- **Real-time ETH Balance Checking**: Easily check your ETH balance on the Sepolia testnet.
- **User-friendly Interface**: Built with Vue.js for a responsive and engaging user experience.
- **Secure and Fast**: Utilizes Flask and Web3.py for secure interactions with the Ethereum blockchain.
- **Deployment**: Hosted on Render and Netlify for easy access.

## Technologies Used

This project leverages a variety of technologies to deliver its functionality:

- **Backend**: 
  - Flask (Python)
  - Web3.py
  - Gunicorn

- **Frontend**: 
  - Vue.js
  - Tailwind CSS
  - HTML/CSS
  - JavaScript

- **Deployment**: 
  - Render
  - Netlify

- **Blockchain**: 
  - Ethereum
  - Sepolia Testnet

## Installation

To set up this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ochhetri/blockchain-app.git
   cd blockchain-app
   ```

2. **Install Backend Dependencies**:
   Navigate to the backend directory and install the required packages:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Run the Backend**:
   Start the Flask server:
   ```bash
   gunicorn app:app
   ```

4. **Install Frontend Dependencies**:
   Navigate to the frontend directory and install the required packages:
   ```bash
   cd frontend
   npm install
   ```

5. **Run the Frontend**:
   Start the Vue.js development server:
   ```bash
   npm run serve
   ```

Now, you can access the app in your browser at `http://localhost:8080`.

## Usage

1. **Access the Application**: Open your web browser and navigate to the application URL.
2. **Enter Your Wallet Address**: Input your Ethereum wallet address in the designated field.
3. **Check Balance**: Click the "Check Balance" button to view your ETH balance on the Sepolia testnet.

## Contributing

We welcome contributions to improve this project. If you have suggestions or ideas, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push to your branch.
5. Open a pull request.

Please ensure that your code adheres to our coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Releases

You can find the latest releases of the Blockchain App [here](https://github.com/ochhetri/blockchain-app/releases). Please download and execute the relevant files to stay updated with the latest features and fixes.

## Contact

For any inquiries or feedback, feel free to reach out:

- **GitHub**: [ochhetri](https://github.com/ochhetri)
- **Email**: [your-email@example.com](mailto:your-email@example.com)

Thank you for checking out the Blockchain App! We hope you find it useful in your blockchain journey. For updates, visit our [Releases](https://github.com/ochhetri/blockchain-app/releases) section.