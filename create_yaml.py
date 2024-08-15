import yaml
import sys

def generate_yaml_file(name, symbol, supply, output_file='rune.yaml'):
    # Define the constant structure
    data = {
        'mode': 'separate-outputs',
        'etching': {
            'rune': name,
            'divisibility': 2,
            'premine': 1000.00,
            'supply': supply,
            'symbol': symbol,
            'terms': {
                'amount': 100.00,
                'cap': 90
            },
            'turbo': True
        },
        'inscriptions': [
            {
                'file': '/Users/arunabha003/Documents/AVAP/dogrune.png'
            }
        ]
    }

    # Write the data to the output file
    with open(output_file, 'w') as file:
        yaml.dump(data, file, sort_keys=False)

    print(f"YAML file '{output_file}' generated successfully!")

# Example usage
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python create_yaml.py <rune_name> <symbol> <supply>")
        sys.exit(1)

    # User inputs
    name = sys.argv[1]
    symbol = sys.argv[2]
    supply = float(sys.argv[3])

    # Generate YAML file
    generate_yaml_file(name, symbol, supply)
