from flask import Flask, jsonify, request, send_from_directory
import subprocess
import re
import json
from etch import run_etch  
from explorer import get_mint_address  
from mine1 import mine_first_block  
from mine2 import mine_second_block  

app = Flask(__name__)

# Route to serve the HTML file
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Route to run ord-env.py
@app.route('/ord-env', methods=['GET', 'POST'])
def run_ord_env():
    try:
        subprocess.run(["python3", "ord-env.py"])
        return jsonify({"message": "ord environment setup completed."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to create the YAML file using create-yaml.py
@app.route('/create-yaml', methods=['POST'])
def create_yaml():
    try:
        data = request.json
        name = data['name']
        symbol = data['symbol']
        supply = data['supply']

        # Call the create-yaml.py script with the provided parameters
        subprocess.run(["python3", "create_yaml.py", name, symbol, str(supply)])
        return jsonify({"message": "YAML file created successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to run etch.py and capture the commitment hash
@app.route('/etch-rune', methods=['GET', 'POST'])
def etch_rune():
    try:
        commit_hash, process = run_etch()
        if commit_hash:
            return jsonify({"commit_hash": commit_hash}), 200
        else:
            raise Exception("Commitment hash not found")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get mint address using the commitment hash
@app.route('/explore', methods=['POST'])
def explore_commit():
    try:
        data = request.json
        commit_hash = data['commit_hash']
        
        # Call the get_mint_address function with the commit hash
        mint_address = get_mint_address(commit_hash)
        
        return jsonify({"mint_address": mint_address}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to run mine1.py using the mint address
@app.route('/mine1', methods=['POST'])
def mine_first_block_route():
    try:
        data = request.json
        mint_address = data['mint_address']
        
        # Call the mine_first_block function with the mint address
        mine_first_block(mint_address)
        return jsonify({"message": "First block mined successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to run mine2.py using the mint address
@app.route('/mine2', methods=['POST'])
def mine_second_block_route():
    try:
        data = request.json
        mint_address = data['mint_address']
        
        # Call the mine_second_block function with the mint address
        mine_second_block(mint_address)
        return jsonify({"message": "Second block mined successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
