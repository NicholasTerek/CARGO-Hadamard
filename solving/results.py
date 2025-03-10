import matplotlib.pyplot as plt
import numpy as np
import re

def read_results(filename):
    matrix_sizes = []
    id3_accuracy = []
    cart_accuracy = []
    
    with open(filename, 'r') as file:
        for line in file:
            match = re.search(r'Original \((\d+)x\d+\) - (ID3|CART) Accuracy: ([0-9\.]+)', line)
            if match:
                size = int(match.group(1))
                algorithm = match.group(2)
                accuracy = float(match.group(3))
                
                if size not in matrix_sizes:
                    matrix_sizes.append(size)
                    id3_accuracy.append(None)
                    cart_accuracy.append(None)
                
                index = matrix_sizes.index(size)
                if algorithm == 'ID3':
                    id3_accuracy[index] = accuracy
                elif algorithm == 'CART':
                    cart_accuracy[index] = accuracy
    
    return matrix_sizes, id3_accuracy, cart_accuracy

def plot_graphs(filename):
    matrix_sizes, id3_accuracy, cart_accuracy = read_results(filename)
    log_matrix_sizes = np.log2(matrix_sizes)  # Convert x-axis to log base 2
    
    # Professional styling
    plt.style.use('seaborn-v0_8-darkgrid')
    
    # Linear scale plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(matrix_sizes, id3_accuracy, marker='o', linestyle='-', label='ID3 Accuracy', linewidth=2)
    ax.plot(matrix_sizes, cart_accuracy, marker='s', linestyle='--', label='CART Accuracy', linewidth=2)
    ax.set_xlabel('Size of Matrix (N)', fontsize=14)
    ax.set_ylabel('Accuracy', fontsize=14)
    ax.set_title(r'$\mathbf{Accuracy\ vs.\ Matrix\ Size}$ (Linear Scale)', fontsize=16)
    ax.set_xticks(matrix_sizes)
    ax.legend(fontsize=12)
    ax.grid(True, linestyle='--', linewidth=0.6)
    plt.show()
    
    # Log scale plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(log_matrix_sizes, id3_accuracy, marker='o', linestyle='-', label='ID3 Accuracy', linewidth=2)
    ax.plot(log_matrix_sizes, cart_accuracy, marker='s', linestyle='--', label='CART Accuracy', linewidth=2)
    ax.set_xlabel(r'$\log_2(\text{Size of Matrix})$', fontsize=14)
    ax.set_ylabel('Accuracy', fontsize=14)
    ax.set_title(r'$\mathbf{Accuracy\ vs.\ Matrix\ Size\ (log_2\ Scale)}$', fontsize=16)
    ax.set_xticks(log_matrix_sizes)
    ax.set_xticklabels([f'$2^{int(x)}$' for x in log_matrix_sizes], fontsize=12)
    ax.legend(fontsize=12)
    ax.grid(True, linestyle='--', linewidth=0.6)
    plt.show()

# Run the plot functions with result.txt
plot_graphs('result.txt')
