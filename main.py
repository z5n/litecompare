import re
import csv

def extract_txids(filename):
    with open(filename, 'r') as file:
        content = file.read()
        return set(re.findall(r'[a-fA-F0-9]{64}', content))

def find_common_txids(file1, file2):
    txids1 = extract_txids(file1)
    txids2 = extract_txids(file2)
    return list(txids1.intersection(txids2))

def save_txids_to_csv(txids, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Transaction ID'])
        for txid in txids:
            writer.writerow([txid])

def main():
    file1 = 'input/address1.csv'
    file2 = 'input/address2.csv'
    output_file = 'output.csv'

    common_txids = find_common_txids(file1, file2)
    save_txids_to_csv(common_txids, output_file)
    print(f"Common txids have been saved to {output_file}")

if __name__ == "__main__":
    main()