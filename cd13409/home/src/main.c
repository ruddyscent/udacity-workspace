/* Include any necessary libraries and header files */
/* Include any necessary libraries and header files */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include "compress.h"
#include "decompress.h"

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
        compress(argv[2]);
    } else if (strcmp(argv[1], "-d") == 0) {
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