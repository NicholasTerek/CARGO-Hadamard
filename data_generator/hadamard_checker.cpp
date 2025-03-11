#include <iostream>
#include <vector>
#include <sstream>
#include <cmath>

// Function to parse input into a vector
std::vector<int> parse_input(const std::string& input) {
    std::vector<int> flat_matrix;
    std::istringstream stream(input);
    int value;

    while (stream >> value) {
        if (value != 1 && value != -1) {
            std::cerr << "Error: Only 1 and -1 are allowed in a Hadamard matrix.\n";
            return {};
        }
        flat_matrix.push_back(value);
    }

    return flat_matrix;
}

// Function to reshape a 1D vector into an NxN matrix
std::vector<std::vector<int>> reshape_to_matrix(const std::vector<int>& flat_matrix) {
    int n = std::sqrt(flat_matrix.size());
    if (n * n != (int)flat_matrix.size()) {
        std::cerr << "Error: Input size is not a perfect square, cannot form an N x N matrix.\n";
        return {};
    }

    std::vector<std::vector<int>> matrix(n, std::vector<int>(n));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            matrix[i][j] = flat_matrix[i * n + j];
        }
    }

    return matrix;
}

// Function to check if a matrix is a Hadamard matrix
bool is_hadamard(const std::vector<std::vector<int>>& matrix) {
    int n = matrix.size();
    if (n == 0) return false;

    // Check orthogonality
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            int dot_product = 0;
            for (int k = 0; k < n; ++k) {
                dot_product += matrix[i][k] * matrix[j][k];
            }
            if (dot_product != 0) {
                std::cerr << "Error: Rows are not orthogonal.\n";
                return false;
            }
        }
    }

    return true;
}

int main() {
    std::string input;
    
    std::cout << "Enter a flattened Hadamard matrix as a single line:\n> ";
    std::getline(std::cin, input);

    std::vector<int> flat_matrix = parse_input(input);
    if (flat_matrix.empty()) return 1;

    std::vector<std::vector<int>> matrix = reshape_to_matrix(flat_matrix);
    if (matrix.empty()) return 1;

    if (is_hadamard(matrix)) {
        std::cout << "✅ This is a valid Hadamard matrix.\n";
    } else {
        std::cerr << "❌ This is NOT a valid Hadamard matrix.\n";
    }

    return 0;
}
