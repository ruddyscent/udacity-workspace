#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "../header_files/compress.h"
#include "../header_files/utils.h"
#include "../header_files/constants.h"

int compress(const char *input_file_name)
{
    printf("Initiated compressing \"%s\"...\n", input_file_name);

    FILE *inputFile = openFile(input_file_name, "r");
    if (inputFile == NULL) {
        printf("Compression of \"%s\" failed\n", input_file_name);
        return 1;
    }

    char base_name[MAX_FILENAME_LENGTH];
    strncpy(base_name, input_file_name, sizeof(base_name) - 1);
    base_name[sizeof(base_name) - 1] = '\0';
    char *dot = strrchr(base_name, '.');
    if (dot != NULL) {
        *dot = '\0';
    }

    char output_file_name[MAX_FILENAME_LENGTH];
    generateUniqueFileName(output_file_name, base_name, "rle");

    FILE *outputFile = openFile(output_file_name, "w");
    if (outputFile == NULL) {
        fclose(inputFile);
        printf("Compression of \"%s\" failed\n", input_file_name);
        return 1;
    }

    int ch, prevCh = EOF, count = 0;
    while ((ch = fgetc(inputFile)) != EOF) {
        if (ch == '\n') {
            if (prevCh != EOF) {
                fprintf(outputFile, "%c%d", prevCh, count);
            }
            fputc('\n', outputFile);
            prevCh = EOF;
            count = 0;
        } else if (ch == prevCh) {
            count++;
        } else {
            if (prevCh != EOF) {
                fprintf(outputFile, "%c%d", prevCh, count);
            }
            prevCh = ch;
            count = 1;
        }
    }

    if (prevCh != EOF) {
        fprintf(outputFile, "%c%d", prevCh, count);
    }

    fclose(inputFile);
    fclose(outputFile);

    printf("Successfully compressed \"%s\" to \"%s\"\n", input_file_name, output_file_name);
    return 0;
}