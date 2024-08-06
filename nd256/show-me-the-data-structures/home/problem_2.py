import os
from typing import List

def find_files(suffix: str, path: str) -> List[str]:
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories.

    Args:
      suffix(str): suffix of the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    files_with_suffix: List[str] = []

    if not os.path.exists(path):
        print(f"The path {path} does not exist.")
        return files_with_suffix

    if not os.path.isdir(path):
        print(f"The path {path} is not a directory.")
        return files_with_suffix

    def recursive_search(current_path: str) -> None:
        try:
            for entry in os.listdir(current_path):
                entry_path = os.path.join(current_path, entry)
                if os.path.isdir(entry_path):
                    # If the entry is a directory, recurse into it
                    recursive_search(entry_path)
                elif os.path.isfile(entry_path) and entry.endswith(suffix):
                    # If it's a file and ends with the suffix, add it to the list
                    files_with_suffix.append(entry_path)
        except PermissionError:
            print(f"Permission denied for accessing {current_path}")

    recursive_search(path)
    return files_with_suffix


if __name__ == "__main__":
    # Test Case 1: Standard test case with known structure
    print("Test Case 1: Standard directory structure")
    result = find_files(".c", "./testdir")
    print(result)
    # Expected output: ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']

    # Test Case 2: Edge case with no .c files
    print("\nTest Case 2: Directory with no .c files")
    os.makedirs("./test_no_c_files", exist_ok=True)
    with open("./test_no_c_files/a.txt", "w") as f:
        f.write("Sample text file.")
    result = find_files(".c", "./test_no_c_files")
    print(result)
    # Expected output: []

    # Test Case 3: Empty directory
    print("\nTest Case 3: Empty directory")
    os.makedirs("./empty_testdir", exist_ok=True)
    result = find_files(".c", "./empty_testdir")
    print(result)
    # Expected output: []

    # Test Case 4: Non-existing directory
    print("\nTest Case 4: Non-existing directory")
    result = find_files(".c", "./non_existing_dir")
    print(result)
    # Expected output: []

    # Test Case 5: Test case with a single .c file at the root level
    print("\nTest Case 5: Directory with a single .c file")
    os.makedirs("./test_single_c_file", exist_ok=True)
    with open("./test_single_c_file/root_file.c", "w") as f:
        f.write("Sample C file.")
    result = find_files(".c", "./test_single_c_file")
    print(result)
    # Expected output: ['./test_single_c_file/root_file.c']