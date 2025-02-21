# File Compression and Decompression Utility

## Overview

This project implements a file compression and decompression utility in C. It provides functionality to compress and decompress files using custom algorithms.

## Features

- Compress files to reduce storage space.

- Decompress previously compressed files.

- Utilizes efficient algorithms for lossless data compression.

- Modular design with separate headers and source files.

## Project Structure
```
project_root/
│── header_files/
│   ├── utils.h
│   ├── constants.h
│   ├── decompress.h
│   ├── compress.h
│── src/
│   ├── main.c
│   ├── compress.c
│   ├── decompress.c
│   ├── utils.c
│   ├── constants.c
│── test_files/
│── Makefile (if available)
│── README.md
```

## Compilation

To compile the project, use the following command:
```bash
gcc -o compressor src/-.c
```

## Usage

To compress a file:
```bash
./compressor -c input.txt
```
To decompress a file:
```bash
./compressor -d output.rle
```

## Dependencies

- GCC compiler

- Standard C libraries

## Future Enhancements

- Support for additional compression formats.

- Multi-threaded compression for improved performance.

- Error handling improvements.

## License

This project is open-source under the MIT License.
