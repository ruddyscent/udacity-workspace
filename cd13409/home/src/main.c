#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "../header_files/compress.h"
#include "../header_files/decompress.h"
#include "../header_files/utils.h"

/**
 * @file main.c
 * @brief Main entry point for the file compression and decompression application.
 *
 * This file contains the main function that serves as the entry point for the
 * application. It handles command-line arguments to perform compression or
 * decompression of files using the specified algorithms.
 */

/**
 * @brief Prints the usage information for the application.
 *
 * This function prints the usage information for the application, including
 * the available options and their descriptions.
 *
 * @param programName The name of the program.
 */
void printUsage(const char *programName);

int main(int argc, char const *argv[])
{
    if (argc == 1) {
        fprintf(stderr, "Error: No arguments given\n");
        printUsage(argv[0]);
        return EXIT_FAILURE;
    }

    if (argc != 3) {
        fprintf(stderr, "Error: Invalid argument(s)\n");
        printUsage(argv[0]);
        return EXIT_FAILURE;
    }

    if (strcmp(argv[1], "-h") == 0) {
        printUsage(argv[0]);
        return EXIT_SUCCESS;
    } else if (strcmp(argv[1], "-c") == 0) {
        if (!checkFileExtension(argv[2], "txt")) {
            fprintf(stderr, "Error: Invalid file type for compression. Expected .txt file\n");
            return EXIT_FAILURE;
        }
        compress(argv[2]);
    } else if (strcmp(argv[1], "-d") == 0) {
        if (!checkFileExtension(argv[2], "rle")) {
            fprintf(stderr, "Error: Invalid file type for decompression. Expected .rle file\n");
            return EXIT_FAILURE;
        }
        decompress(argv[2]);
    } else {
        fprintf(stderr, "Error: Invalid option: %s\n", argv[1]);
        printUsage(argv[0]);
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}

void printUsage(const char *programName) {
    fprintf(stderr, "Usage: %s -c <input.txt> | -d <input.rle> | -h\n", programName);
    fprintf(stderr, "Options:\n");
    fprintf(stderr, "  -c <input.txt>    Compress the specified text file\n");
    fprintf(stderr, "  -d <input.rle>    Decompress the specified RLE file\n");
    fprintf(stderr, "  -h                Display this help message\n");
}