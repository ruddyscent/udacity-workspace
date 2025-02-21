#include "../header_files/utils.h"
#include "../header_files/constants.h"
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

FILE* openFile(const char *file_name, const char *mode) {
    FILE *file = fopen(file_name, mode);
    if (file == NULL) {
        perror("Error opening file");
    }
    return file;
}

void generateUniqueFileName(char *output_file_name, const char *base_name, const char *extension) {
    snprintf(output_file_name, 256, "%s.%s", base_name, extension);
    int version = 0;
    while (access(output_file_name, F_OK) == 0) {
        version++;
        snprintf(output_file_name, 256, "%s_%d.%s", base_name, version, extension);
    }
}