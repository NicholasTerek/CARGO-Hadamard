import numpy as np
import random

def generate_hadamard(n):
    """Generates an n x n Hadamard matrix using Sylvester's recursive construction."""
    if n == 1:
        return np.array([[1]])
    H_small = generate_hadamard(n // 2)
    return np.block([[H_small, H_small], [H_small, -H_small]])

def apply_random_operations(H, num_operations=10):
    """Applies random row/column swaps and sign flips to diversify Hadamard matrices."""
    size = H.shape[0]
    H = H.copy()
    
    for _ in range(num_operations):
        op_type = random.choice(["row_swap", "col_swap", "row_flip", "col_flip"])
        i, j = random.sample(range(size), 2)
        
        if op_type == "row_swap":
            H[[i, j], :] = H[[j, i], :]
        elif op_type == "col_swap":
            H[:, [i, j]] = H[:, [j, i]]
        elif op_type == "row_flip":
            H[i, :] *= -1
        elif op_type == "col_flip":
            H[:, i] *= -1
    
    return H

def generate_large_dataset(matrix_size, num_samples):
    """Generates a dataset of Hadamard matrices with random transformations."""
    base_H = generate_hadamard(matrix_size)
    dataset = [apply_random_operations(base_H, num_operations=10) for _ in range(num_samples)]
    return dataset

def matrix_to_binary_string(H):
    """Convert Hadamard matrix (-1,1) to a single binary string (0,1)."""
    return ''.join(['1' if x == 1 else '0' for x in H.flatten()])

def matrix_to_decimal(H):
    """Convert Hadamard matrix (-1,1) to decimal representation per row."""
    binary_rows = [''.join(['1' if x == 1 else '0' for x in row]) for row in H]
    return [int(row, 2) for row in binary_rows]  # Convert binary string to decimal

def matrix_to_original_string(H):
    """Convert Hadamard matrix (-1,1) to a single line string."""
    return ' '.join(map(str, H.flatten()))

# Generate Hadamard datasets for multiple sizes
sizes = [4, 8, 16, 32, 64, 128, 256, 512]
num_samples = 2000  # Generate 2000 matrices per size

for size in sizes:
    print(f"Generating {num_samples} Hadamard matrices of size {size}x{size}...")
    dataset = generate_large_dataset(size, num_samples)

    # Convert to different representations
    binary_strings = [matrix_to_binary_string(H) for H in dataset]
    decimal_representations = [matrix_to_decimal(H) for H in dataset]
    original_strings = [matrix_to_original_string(H) for H in dataset]

    # Save to files
    with open(f"hadamard_matrices_{size}_binary.txt", "w") as f:
        for binary_string in binary_strings:
            f.write(binary_string + "\n")

    np.savetxt(f"hadamard_matrices_{size}_decimal.txt", decimal_representations, fmt='%d', delimiter=" ")

    with open(f"hadamard_matrices_{size}_original.txt", "w") as f:
        for original_string in original_strings:
            f.write(original_string + "\n")

    print(f"Saved {num_samples} Hadamard matrices of size {size}x{size}.")

print("All Hadamard datasets generated and saved!")
