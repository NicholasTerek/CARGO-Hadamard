import matplotlib.pyplot as plt
import numpy as np
import re
import sys

def read_results(filename):
    """Reads and parses accuracy results from the given file."""
    data = {}  # Dictionary to store results by (size, ops)

    try:
        with open(filename, 'r') as file:
            for line in file:
                match = re.search(r'Original \((\d+)x\d+, (\d+) ops\) - (ID3|CART) Accuracy: ([0-9\.]+)', line)
                if match:
                    size = int(match.group(1))
                    ops = int(match.group(2))
                    algorithm = match.group(3)
                    accuracy = float(match.group(4))

                    if (size, ops) not in data:
                        data[(size, ops)] = {'ID3': None, 'CART': None}

                    data[(size, ops)][algorithm] = accuracy
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found. Please check the path.")
        sys.exit(1)

    return data

def plot_graphs(filename):
    """Generates professional accuracy plots from results file."""
    data = read_results(filename)
    
    # Extract unique sizes and operations
    matrix_sizes = sorted(set(size for size, _ in data.keys()))
    operations = sorted(set(ops for _, ops in data.keys()))

    # Prepare accuracy storage
    id3_accuracy = {ops: [] for ops in operations}
    cart_accuracy = {ops: [] for ops in operations}

    for size in matrix_sizes:
        for ops in operations:
            if (size, ops) in data:
                id3_accuracy[ops].append(data[(size, ops)]['ID3'])
                cart_accuracy[ops].append(data[(size, ops)]['CART'])
            else:
                id3_accuracy[ops].append(None)
                cart_accuracy[ops].append(None)

    # 🔹 Plot 1: ID3 Accuracy vs. Matrix Size (Different Operation Counts)
    plt.figure(figsize=(10, 6))
    for ops in operations:
        plt.plot(matrix_sizes, id3_accuracy[ops], marker='o', linestyle='-', label=f"{ops} Ops", linewidth=2)

    plt.xscale('log', base=2)
    plt.xticks(matrix_sizes, labels=[f"$2^{int(np.log2(s))}$" for s in matrix_sizes])
    plt.xlabel("Matrix Size (N)", fontsize=14)
    plt.ylabel("Accuracy", fontsize=14)
    plt.title(r'$\mathbf{ID3\ Accuracy\ vs.\ Matrix\ Size}$ (Different Ops)', fontsize=16)
    plt.legend(title="Operations", fontsize=12)
    plt.grid(True, linestyle='--', linewidth=0.6)
    plt.show()

    # 🔹 Plot 2: ID3 & CART Accuracy vs. Matrix Size
    plt.figure(figsize=(10, 6))
    for ops in operations:
        plt.plot(matrix_sizes, id3_accuracy[ops], marker='o', linestyle='-', label=f"ID3 - {ops} Ops", linewidth=2)
        plt.plot(matrix_sizes, cart_accuracy[ops], marker='s', linestyle='--', label=f"CART - {ops} Ops", linewidth=2)

    plt.xscale('log', base=2)
    plt.xticks(matrix_sizes, labels=[f"$2^{int(np.log2(s))}$" for s in matrix_sizes])
    plt.xlabel("Matrix Size (N)", fontsize=14)
    plt.ylabel("Accuracy", fontsize=14)
    plt.title(r'$\mathbf{ID3\ &\ CART\ Accuracy\ vs.\ Matrix\ Size}$', fontsize=16)
    plt.legend(title="Operations", fontsize=12, loc="lower right")
    plt.grid(True, linestyle='--', linewidth=0.6)
    plt.show()

    # 🔹 Plot 3: ID3 & CART Accuracy vs. Number of Operations (Largest Matrix)
    largest_size = matrix_sizes[-1]
    plt.figure(figsize=(10, 6))
    plt.plot(operations, [id3_accuracy[ops][-1] for ops in operations], marker='o', linestyle='-', label="ID3", linewidth=2)
    plt.plot(operations, [cart_accuracy[ops][-1] for ops in operations], marker='s', linestyle='--', label="CART", linewidth=2)

    plt.xscale('log', base=10)
    plt.xticks(operations, labels=[str(o) for o in operations])
    plt.xlabel("Number of Operations", fontsize=14)
    plt.ylabel("Accuracy", fontsize=14)
    plt.title(fr'$\mathbf{{ID3\ &\ CART\ Accuracy\ vs.\ Ops}}$ ({largest_size}x{largest_size})', fontsize=16)
    plt.legend(fontsize=12)
    plt.grid(True, linestyle='--', linewidth=0.6)
    plt.show()

# 🔹 Run the script with a command-line argument
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("❌ Usage: python resultsV2.py <path_to_result_file>")
        sys.exit(1)

    result_file = sys.argv[1]
    plot_graphs(result_file)
