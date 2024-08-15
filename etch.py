import subprocess
import re

def run_etch():
    process = subprocess.Popen(
        ["ord", "--data-dir", "env", "wallet", "batch", "--batch", "rune.yaml", "--fee-rate", "1"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    commit_hash = None

    # Process output line by line
    for line in process.stdout:
        print(line.strip())  # Print or log each line for debugging
        if "commitment" in line.lower() and commit_hash is None:  # Only capture the first occurrence
            commit_hash_match = re.search(r'commitment\s+([a-f0-9]+)', line)
            if commit_hash_match:
                commit_hash = commit_hash_match.group(1)
                print(f"Commitment Hash: {commit_hash}")
                break  # Exit the loop after capturing the first commit hash

    # At this point, commit_hash contains the hash or is None if not found
    return commit_hash, process

# Example usage:
if __name__ == "__main__":
    commit_hash, process = run_etch()
    if commit_hash:
        print(f"Commitment Hash: {commit_hash}")
        # Optionally continue to monitor the process
        process.wait()  # Wait for the process to complete if needed
    else:
        print("Commitment hash not found.")
