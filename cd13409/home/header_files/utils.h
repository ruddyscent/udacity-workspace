#ifndef UTILS_H
#define UTILS_H

#include <stdio.h>

FILE* openFile(const char *file_name, const char *mode);
void generateUniqueFileName(char *output_file_name, const char *base_name, const char *extension);

#endif // UTILS_H