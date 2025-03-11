#include "hadamard.h"
#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <sstream>
#include <bitset>

// Function to generate Hadamard matrix using Sylvester's recursive method
Matrix generate_hadamard(int n) {
    if (n == 1) {
        return {{1}};
    }
    
    Matrix H_small = generate_hadamard(n / 2);
    Matrix H(n, std::vector<int>(n));

    for (int i = 0; i < n / 2; i++) {
        for (int j = 0; j < n / 2; j++) {
            H[i][j] = H_small[i][j];
            H[i][j + n / 2] = H_small[i][j];
            H[i + n / 2][j] = H_small[i][j];
            H[i + n / 2][j + n / 2] = -H_small[i][j];
        }
    }
    
    return H;
}

// Function to apply random row/column swaps and sign flips
Matrix apply_random_operations(const Matrix& H, int num_operations) {
    Matrix modified_H = H;
    int size = H.size();
    
    for (int op = 0; op < num_operations; ++op) {
        int i = rand() % size;
        int j = rand() % size;
        int op_type = rand() % 4;

        switch (op_type) {
            case 0: // Row swap
                std::swap(modified_H[i], modified_H[j]);
                break;
            case 1: // Column swap
                for (int k = 0; k < size; ++k) {
                    std::swap(modified_H[k][i], modified_H[k][j]);
                }
                break;
            case 2: // Row flip
                for (int k = 0; k < size; ++k) {
                    modified_H[i][k] *= -1;
                }
                break;
            case 3: // Column flip
                for (int k = 0; k < size; ++k) {
                    modified_H[k][i] *= -1;
                }
                break;
        }
    }

    return modified_H;
}

// Convert Hadamard matrix to a binary string (0,1)
std::string matrix_to_binary_string(const Matrix& H) {
    std::ostringstream binary_string;
    for (const auto& row : H) {
        for (int val : row) {
            binary_string << (val == 1 ? '1' : '0');
        }
    }
    return binary_string.str();
}

// Convert Hadamard matrix to decimal representation per row
std::vector<int> matrix_to_decimal(const Matrix& H) {
    std::vector<int> decimal_representation;
    for (const auto& row : H) {
        std::string binary_row;
        for (int val : row) {
            binary_row += (val == 1 ? '1' : '0');
        }
        decimal_representation.push_back(std::stoi(binary_row, nullptr, 2));
    }
    return decimal_representation;
}

// Convert Hadamard matrix to original format (-1,1) as a string
std::string matrix_to_original_string(const Matrix& H) {
    std::ostringstream original_string;
    for (const auto& row : H) {
        for (int val : row) {
            original_string << val << " ";
        }
    }
    return original_string.str();
}