#ifndef UTILS_H
#define UTILS_H

#include <stdio.h>

/**
 * @file utils.h
 * @brief Utility functions for file operations and name generation.
 *
 * This header file contains utility function declarations for opening files,
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
FILE* openFile(const char *file_name, const char *mode);

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
void generateUniqueFileName(char *output_file_name, const char *base_name, const char *extension);

/**
 * @brief Checks if the file has the specified extension.
 *
 * This function checks if the given file name has the specified extension.
 *
 * @param file_name The name of the file to check.
 * @param extension The expected extension of the file.
 * @return int Returns 1 if the file has the specified extension, 0 otherwise.
 */
int checkFileExtension(const char *file_name, const char *extension);

#endif // UTILS_H