#ifndef HADAMARD_H
#define HADAMARD_H

#include <vector>
#include <string>

using Matrix = std::vector<std::vector<int>>;

/**
 * @brief Generates an n x n Hadamard matrix using Sylvester's recursive construction.
 * 
 * @param n The size of the matrix (must be a power of 2).
 * @return A Hadamard matrix of size n x n.
 */
Matrix generate_hadamard(int n);

/**
 * @brief Applies random row/column swaps and sign flips to a Hadamard matrix.
 * 
 * @param H The input Hadamard matrix.
 * @param num_operations The number of random modifications to apply.
 * @return A modified Hadamard matrix.
 */
Matrix apply_random_operations(const Matrix& H, int num_operations);

/**
 * @brief Converts a Hadamard matrix to a binary string representation (0 and 1).
 * 
 * @param H The input Hadamard matrix.
 * @return A string representing the matrix in binary form.
 */
std::string matrix_to_binary_string(const Matrix& H);

/**
 * @brief Converts each row of a Hadamard matrix into a decimal number.
 * 
 * @param H The input Hadamard matrix.
 * @return A vector of integers representing the decimal values of each row.
 */
std::vector<int> matrix_to_decimal(const Matrix& H);

/**
 * @brief Converts a Hadamard matrix into a string representation with original values (-1 and 1).
 * 
 * @param H The input Hadamard matrix.
 * @return A string where the matrix is flattened into space-separated values.
 */
std::string matrix_to_original_string(const Matrix& H);

#endif
