import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import os

# Load Data Function
def load_original_data(filename, size):
    """Loads an original Hadamard matrix file and prepares it for training."""
    X, y = [], []
    with open(filename, 'r') as f:
        for line in f:
            values = list(map(int, line.strip().split()))
            H = np.array(values).reshape((size, size))  
            for col in range(size):
                X.append(H[:size-1, col])  
                y.append(H[size-1, col])  
    return np.array(X), np.array(y)

# Train and evaluate both ID3 (entropy) and CART (gini) decision trees
def train_and_evaluate(X, y, name, size, ops, test_size=0.2, max_depth=None):
    """Trains and evaluates both an ID3 (entropy) and a CART (gini) decision tree classifier."""
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=test_size, random_state=42)

    # ID3 Decision Tree (uses "entropy" as the criterion)
    clf_id3 = DecisionTreeClassifier(criterion="entropy", max_depth=max_depth, random_state=42)
    clf_id3.fit(X_train, y_train)
    acc_id3 = accuracy_score(y_val, clf_id3.predict(X_val))

    # CART Decision Tree (uses "gini" as the criterion)
    clf_cart = DecisionTreeClassifier(criterion="gini", max_depth=max_depth, random_state=42)
    clf_cart.fit(X_train, y_train)
    acc_cart = accuracy_score(y_val, clf_cart.predict(X_val))

    print(f"{name} ({size}x{size}, {ops} ops) - ID3 Accuracy: {acc_id3:.4f}")
    print(f"{name} ({size}x{size}, {ops} ops) - CART Accuracy: {acc_cart:.4f}")

# Main execution
if __name__ == "__main__":
    sizes = [4, 8, 16, 32, 64, 128, 256, 512]  
    operations = [10, 20, 40, 80, 160, 320, 640]  
    data_folder = "C:/Users/nicky/OneDrive/Desktop/CARGO/data/"

    for size in sizes:
        print("_______________________________")
        for ops in operations:
            original_file = os.path.join(data_folder, f"datahadamard_matrices_{size}_ops{ops}.txt")

            if os.path.exists(original_file):
                # print(f"Processing {original_file}...")
                X_original, y_original = load_original_data(original_file, size)
                train_and_evaluate(X_original, y_original, "Original", size, ops, max_depth=5)
            else:
                print(f"Skipping {original_file} (file not found).")
