### README: How to Run the Ordinals Automation Interface

This project provides a web interface to automate various Ordinals-related tasks, including setting up the environment, creating a YAML file, etching a rune, retrieving the mint address, and mining blocks.

#### **Prerequisites**
- **Python 3.x** installed on your system
- **Flask** web framework installed (`pip install flask`)
- **Selenium** installed for web automation (`pip install selenium`)
- **ChromeDriver** installed and in your system's PATH
- **Ordinals CLI** and **Bitcoin Core** installed via Homebrew

#### **Steps to Install Ordinals CLI and Bitcoin Core**

1. **Install Homebrew** (if not already installed):
   - Homebrew is a package manager for macOS and Linux. Install it using:
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```

2. **Install Bitcoin Core**:
   - Install Bitcoin Core via Homebrew:
     ```bash
     brew install bitcoin
     ```
   - Start Bitcoin Core:
     ```bash
     bitcoind -daemon
     ```
   - You can interact with Bitcoin Core using `bitcoin-cli`. For example:
     ```bash
     bitcoin-cli getblockchaininfo
     ```

3. **Install Ordinals CLI**:
   - First, ensure you have Rust installed:
     ```bash
     brew install rust
     ```
   - Then install the Ordinals CLI via Homebrew:
     ```bash
     brew install ord
     ```
   - Verify the installation:
     ```bash
     ord --version
     ```

#### **Steps to Run**

1. **Clone the Repository**
   - Clone or download the repository containing the project files.

2. **Install Python Dependencies**
   - Ensure you have installed all necessary Python packages:
     ```bash
     pip install flask selenium
     ```

3. **Start the Flask Server**
   - Navigate to the directory containing `app.py` and start the Flask server:
     ```bash
     python3 app.py
     ```
   - The server will start on `http://localhost:5000`.

4. **Access the Web Interface**
   - Open your web browser and go to `http://localhost:5000` to access the Ordinals Automation Interface.

5. **Use the Web Interface**
   - **Start Server**: Click the "Start Server" button to initialize the Ordinals environment.
   - **Create YAML**: Fill in the fields (rune name=min 13 char in capital, symbol, supply=10000) and click "Create YAML" to generate the YAML file.
   - **Etch a Rune**: Click "Etch Rune" to start the rune etching process. The commitment hash will be displayed once available.
   - **Get Mint Address**: Enter the commitment hash and click "Get Mint Address" to retrieve the address.
   - **Mine First Block**: Enter the mint address and click "Mine First Block" to mine the required block.
   - **Mine Second Block**: Enter the mint address and click "Mine Second Block" to complete the mining process.
   - **View Runes**: Click the "View Runes" button to navigate to the Ordinals explorer at `http://0.0.0.0:9001/runes`.

6. **Stop the Flask Server**
   - To stop the server, press `Ctrl + C` in the terminal where the Flask server is running.

#### **Additional Notes**
- Ensure that all required services, such as the Ordinals explorer, are running on their respective ports before starting the operations.


