#include "hadamard.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <array>
#include <cstdlib>
#include <ctime>
#include <chrono>
#include <filesystem>  

namespace fs = std::filesystem;

// Constants for easy modification
constexpr std::array<int, 8> MATRIX_SIZES = {4, 8, 16, 32, 64, 128, 256, 512};
constexpr int NUM_SAMPLES = 2000;
constexpr int NUM_OPERATIONS = 640;

int main() {
    srand(time(0));

    // Ensure "data" folder exists
    std::string data_folder = "C:/Users/nicky/OneDrive/Desktop/CARGO/data";
    if (!fs::exists(data_folder)) {
        fs::create_directory(data_folder);
    }

    std::cout << "Program started.\n";

    for (int size : MATRIX_SIZES) {
        std::cout << "Generating " << NUM_SAMPLES << " Hadamard matrices of size " 
                  << size << "x" << size << " with " << NUM_OPERATIONS << " random operations...\n";

        // Start measuring total time
        auto total_start = std::chrono::high_resolution_clock::now();

        // Start measuring matrix generation time
        auto gen_start = std::chrono::high_resolution_clock::now();

        // Generate matrices
        std::vector<Matrix> matrices;
        matrices.reserve(NUM_SAMPLES);
        for (int i = 0; i < NUM_SAMPLES; ++i) {
            Matrix H = generate_hadamard(size);
            H = apply_random_operations(H, NUM_OPERATIONS);
            matrices.push_back(std::move(H));
        }

        // End matrix generation timing
        auto gen_end = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double> gen_time = gen_end - gen_start;
        std::cout << "Matrix generation completed in " << gen_time.count() << " seconds.\n";

        // Start measuring file writing time
        auto write_start = std::chrono::high_resolution_clock::now();

        // Construct filename inside "data" folder
        std::string filename = data_folder + "hadamard_matrices_" + std::to_string(size) + 
                               "_ops" + std::to_string(NUM_OPERATIONS) + ".txt";
        std::ofstream output_file(filename);

        for (const auto& H : matrices) {
            output_file << matrix_to_original_string(H) << "\n"; // Ensure single-line format
        }

        output_file.close();

        // End file writing timing
        auto write_end = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double> write_time = write_end - write_start;
        std::cout << "File writing completed in " << write_time.count() << " seconds.\n";

        // End measuring total time
        auto total_end = std::chrono::high_resolution_clock::now();
        std::chrono::duration<double> total_time = total_end - total_start;
        std::cout << "Finished processing size " << size << " in " << total_time.count() << " seconds.\n";
    }

    std::cout << "Program finished execution.\n";
    return 0;
}
