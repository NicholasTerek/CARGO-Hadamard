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
def train_and_evaluate(X_train, y_train, X_test, y_test, name, max_depth=None):
    """Trains and evaluates both an ID3 (entropy) and a CART (gini) decision tree classifier."""
    # ID3 Decision Tree (Entropy)
    clf_id3 = DecisionTreeClassifier(criterion="entropy", max_depth=max_depth, random_state=42)
    clf_id3.fit(X_train, y_train)
    acc_id3 = accuracy_score(y_test, clf_id3.predict(X_test))
    
    # CART Decision Tree (Gini)
    clf_cart = DecisionTreeClassifier(criterion="gini", max_depth=max_depth, random_state=42)
    clf_cart.fit(X_train, y_train)
    acc_cart = accuracy_score(y_test, clf_cart.predict(X_test))
    
    print(f"{name} - ID3 Accuracy: {acc_id3:.4f}")
    print(f"{name} - CART Accuracy: {acc_cart:.4f}")

# Main execution
if __name__ == "__main__":
    size = 8  # Adjust if needed
    data_folder = "C:/Users/nicky/OneDrive/Desktop/CARGO/data/"
    
    train_file_sylvester = os.path.join(data_folder, "Sylvester_hadamard_dataset.txt")
    test_file_paley = os.path.join(data_folder, "Paley_hadamard_dataset.txt")
    
    if os.path.exists(train_file_sylvester) and os.path.exists(test_file_paley):
        # Load datasets
        X_sylvester, y_sylvester = load_original_data(train_file_sylvester, size)
        X_paley, y_paley = load_original_data(test_file_paley, size)
        
        # Perform 70/30 split on Sylvester dataset
        X_train_syl, X_val_syl, y_train_syl, y_val_syl = train_test_split(X_sylvester, y_sylvester, test_size=0.3, random_state=42)
        train_and_evaluate(X_train_syl, y_train_syl, X_val_syl, y_val_syl, "Sylvester 70/30 Split", max_depth=5)
        
        # Perform 70/30 split on Paley dataset
        X_train_pal, X_val_pal, y_train_pal, y_val_pal = train_test_split(X_paley, y_paley, test_size=0.3, random_state=42)
        train_and_evaluate(X_train_pal, y_train_pal, X_val_pal, y_val_pal, "Paley 70/30 Split", max_depth=5)
        
        # Train on Paley, test on Sylvester
        train_and_evaluate(X_paley, y_paley, X_sylvester, y_sylvester, "Paley 100% Train, Sylvester Test", max_depth=5)
        
        # Train on Sylvester, test on Paley
        train_and_evaluate(X_sylvester, y_sylvester, X_paley, y_paley, "Sylvester 100% Train, Paley Test", max_depth=5)
    else:
        print("One or both dataset files are missing.")
