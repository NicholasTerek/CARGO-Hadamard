import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
import os

# START WITH OVERLEAF
#Take away more rows 2 rows, starting from 64 removing 3 rows -> the more rows we take away, the more coloumns are depenetented (4 becauses more complicanted)
#how does it behavour when you increase the size(dataset more then 2000) -> maybe 64 how that respoments to greater dataset
#expermental 
# differnt constructs, we can use sylverstor consturstions and 
# 8x8 only has 3 types so we can use this as to test it agaist different contrsution and 32 (2 circleents matrix(lazends pairs))
# maybe test equaivlences -> group theory? 

# Load Data Functions
def load_original_data(filename, size):
    X, y = [], []
    with open(filename, 'r') as f:
        for line in f:
            values = list(map(int, line.strip().split()))
            H = np.array(values).reshape((size, size))  
            for col in range(size):
                X.append(H[:size-1, col])  
                y.append(H[size-1, col])  
    return np.array(X), np.array(y)

def load_binary_data(filename, size):
    X, y = [], []
    with open(filename, 'r') as f:
        for line in f:
            binary_str = line.strip()
            H = np.array([list(binary_str[i*size:(i+1)*size]) for i in range(size)], dtype=int)
            for col in range(size):
                X.append(H[:size-1, col])  
                y.append(H[size-1, col])  
    return np.array(X), np.array(y)

def load_decimal_data(filename, size):
    X, y = [], []
    with open(filename, 'r') as f:
        for line in f:
            decimals = list(map(int, line.strip().split()))
            H_rows = [list(format(d, f'0{size}b')) for d in decimals]  # Convert decimal to binary
            H = np.array([[int(bit) for bit in row] for row in H_rows])
            for col in range(size):
                X.append(H[:size-1, col])  
                y.append(H[size-1, col])  
    return np.array(X), np.array(y)

# Train and evaluate decision trees
def train_and_evaluate(X, y, name, size, test_size=0.2, max_depth=None):
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=test_size, random_state=42)

    # ID3 Decision Tree
    clf_id3 = DecisionTreeClassifier(criterion="entropy", max_depth=max_depth, random_state=42)
    clf_id3.fit(X_train, y_train)
    acc_id3 = accuracy_score(y_val, clf_id3.predict(X_val))

    # CART Decision Tree
    clf_cart = DecisionTreeClassifier(criterion="gini", max_depth=max_depth, random_state=42)
    clf_cart.fit(X_train, y_train)
    acc_cart = accuracy_score(y_val, clf_cart.predict(X_val))

    print(f"{name} ({size}x{size}) - ID3 Accuracy: {acc_id3:.4f}")
    print(f"{name} ({size}x{size}) - CART Accuracy: {acc_cart:.4f}")

    # Visualize Trees
    fig, axes = plt.subplots(1, 2, figsize=(18, 5))
    for i, (clf, title) in enumerate(zip([clf_id3, clf_cart], ["ID3", "CART"])):
        plot_tree(clf, filled=True, ax=axes[i], feature_names=[f'F{i}' for i in range(X.shape[1])], class_names=["0", "1"])
        axes[i].set_title(f"{name} ({size}x{size}) - {title}")
    plt.show()

# Main execution
if __name__ == "__main__":
    sizes = [4, 8, 16, 32, 64, 128, 256, 512]  
    
    for size in sizes:
        original_file = f"hadamard_matrices_{size}_original.txt"
        binary_file = f"hadamard_matrices_{size}_binary.txt"
        decimal_file = f"hadamard_matrices_{size}_decimal.txt"

        if os.path.exists(original_file):
            X_original, y_original = load_original_data(original_file, size)
            train_and_evaluate(X_original, y_original, "Original", size, max_depth=5)
    """
        if os.path.exists(binary_file):
            X_binary, y_binary = load_binary_data(binary_file, size)
            train_and_evaluate(X_binary, y_binary, "Binary", size, max_depth=5)

        if os.path.exists(decimal_file):
            X_decimal, y_decimal = load_decimal_data(decimal_file, size)
            train_and_evaluate(X_decimal, y_decimal, "Decimal", size, max_depth=5)
    """