#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#include "../header_files/utils.h"
#include "../header_files/constants.h"

/**
 * @file utils.c
 * @brief Implementation of utility functions for file operations and name generation.
 *
 * This file contains the implementation of utility functions for opening files,
 * generating unique file names, and checking file extensions.
 */

/**
 * @brief Opens a file with the specified mode.
 *
 * This function opens a file with the given name and mode, and returns a file pointer.
 * If the file cannot be opened, an error message is printed.
 *
 * @param file_name The name of the file to be opened.
 * @param mode The mode in which to open the file.
 * @return FILE* A pointer to the opened file, or NULL if the file could not be opened.
 */
FILE* openFile(const char *file_name, const char *mode) {
    FILE *file = fopen(file_name, mode);
    if (file == NULL) {
        perror("Error opening file");
    }
    return file;
}

/**
 * @brief Generates a unique file name by appending a version number if necessary.
 *
 * This function generates a unique file name based on the given base name and extension.
 * If a file with the generated name already exists, an underscore and a version number
 * are appended to the base name until a unique name is found.
 *
 * @param output_file_name The buffer to store the generated file name.
 * @param base_name The base name of the file.
 * @param extension The extension of the file.
 */
void generateUniqueFileName(char *output_file_name, const char *base_name, const char *extension) {
    snprintf(output_file_name, MAX_FILENAME_LENGTH, "%s.%s", base_name, extension);
    int version = 0;
    while (access(output_file_name, F_OK) == 0) {
        version++;
        snprintf(output_file_name, MAX_FILENAME_LENGTH, "%s_%d.%s", base_name, version, extension);
    }
}

/**
 * @brief Checks if the file has the specified extension.
 *
 * This function checks if the given file name has the specified extension.
 *
 * @param file_name The name of the file to check.
 * @param extension The expected extension of the file.
 * @return int Returns 1 if the file has the specified extension, 0 otherwise.
 */
int checkFileExtension(const char *file_name, const char *extension) {
    const char *dot = strrchr(file_name, '.');
    if (!dot || dot == file_name) return 0;
    return strcmp(dot + 1, extension) == 0;
}