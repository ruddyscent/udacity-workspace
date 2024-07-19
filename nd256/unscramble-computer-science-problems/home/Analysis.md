## Task0.py

1. **Reading the files (`texts.csv` and `calls.csv`):** The time complexity of reading a file is O(N), where N is the number of lines in the file. This is because each line must be read and processed. Since there are two files, if we assume `texts.csv` has `N` lines and `calls.csv` has `M` lines, the complexity for this part is O(N + M).

2. **Converting the file contents to lists:** The `list(reader)` operation converts the iterable returned by `csv.reader` into a list. This operation is also O(N) for each file, as it must iterate through each item produced by the reader. Thus, for both files together, this remains O(N + M).

3. **Accessing the first and last records of the lists:** Accessing an element in a list by index is an O(1) operation. Therefore, accessing the first record of `texts` and the last record of `calls` does not significantly add to the overall time complexity.

4. **Printing the records:** The time complexity of printing is generally considered O(1) for a fixed-size output, which is the case here. However, it's worth noting that the actual time taken can vary based on the environment and is generally not considered in algorithmic complexity analysis.

Combining these, the overall worst-case time complexity of the script is dominated by the file reading and list conversion steps, leading to a final complexity of **O(N + M)**, where `N` is the number of records in `texts.csv` and `M` is the number of records in `calls.csv`.

## Task1.py

1. **Initialization of a set (`telephones`):** This is an O(1) operation, as it simply initializes an empty set.

2. **Iterating over `texts` and `calls` records and adding telephone numbers to the set:** 
   - The `for` loop iterates over each record in `texts` and `calls`. Let's denote the number of records in `texts` as `N` and in `calls` as `M`.
   - For each iteration, two `add` operations are performed – one for each telephone number in the record (sender and receiver). The `add` operation for a set in Python is generally O(1), assuming a good hash function and that the hash table does not need to be resized too often. However, in the worst case (e.g., when a resize occurs), it could temporarily be O(n), but this is rare and amortized over many additions to be considered O(1) for each addition.
   - Therefore, for both loops combined, if we consider the `add` operation as O(1) in average case, the total complexity for this part is O(N + M).

3. **Calculating the length of the set and printing the result:** 
   - The `len` function is O(1) as it simply returns the count of elements in the set, which is maintained with the set's metadata.
   - The `print` function's complexity is not typically considered in algorithmic complexity analysis, as it is dependent on the environment and is generally O(1) for practical purposes.

Combining these, the overall worst-case time complexity of the script is dominated by the loops that iterate over `texts` and `calls`, leading to a final complexity of **O(N + M)**. This represents the time to iterate over all records in both `texts` and `calls` and add their telephone numbers to the set, where `N` is the number of records in `texts` and `M` is the number of records in `calls`.

## Task2.py

1. **Initialization of a defaultdict (`duration`):** This is an O(1) operation, as it simply initializes an empty defaultdict with integers.

2. **Iterating over `calls` records and updating `duration`:**
   - Let's denote the number of records in `calls` as `N`.
   - The loop iterates over each record in `calls`. For each iteration, it performs two update operations on the `duration` defaultdict.
   - Updating the defaultdict for a key (either adding a new key or updating an existing one) is generally considered an O(1) operation, assuming a good hash function and that the hash table does not need to be resized too often. However, in the worst case (e.g., when a resize occurs), it could temporarily be O(n), but this is rare and amortized over many additions to be considered O(1) for each addition.
   - Therefore, for the loop, the total complexity is O(2N) = O(N), as each record involves two O(1) operations.

3. **Finding the maximum duration:**
   - The `max` function with a key argument iterates over each item in `duration.items()`, which in this case, will be `N` items if all calls are between unique pairs, or fewer if some numbers are repeated.
   - The iteration itself is O(N), as it needs to check each item once to determine the maximum.
   - The lambda function provided to the `key` argument is O(1) for each item, as it simply returns the value part of the tuple.

4. **Printing the result:** The complexity of the `print` function is not typically considered in algorithmic complexity analysis, as it is dependent on the environment and is generally O(1) for practical purposes.

Combining these steps, the overall worst-case time complexity of the script is **O(N)**. This represents the time to iterate over all records in `calls`, update the `duration` for each number, and then find the number with the maximum duration.

## Task3.py

1. **Initialization of variables (`from_bangalore`, `to_bangalore`):** This is an O(1) operation, as it simply sets two integer variables to 0.

2. **Iterating over `calls` records:**
   - Let's denote the number of records in `calls` as `N`.
   - The loop iterates over each record in `calls`. For each iteration, it performs a constant-time check to see if the call is from Bangalore (i.e., `record[0][:5] != "(080)"`). This string comparison is O(1) because the substring length is constant (5 characters).
   - If the call is from Bangalore, `from_bangalore` is incremented by 1, which is an O(1) operation.
   - Then, it checks if the call is not to Bangalore (i.e., `record[1][:5] != "(080)"`). This is another O(1) operation for the same reason as above.
   - If the call is not to Bangalore, `to_bangalore` is incremented by 1, which is also an O(1) operation.

3. **Calculating the percentage and printing the result:**
   - The calculation of `float(to_bangalore) / from_bangalore` is an O(1) operation, as it involves a single division of two integers.
   - The `print` function's complexity is not typically considered in algorithmic complexity analysis, as it is dependent on the environment and is generally O(1) for practical purposes.

Combining these steps, the overall worst-case time complexity of the script is **O(N)**. This represents the time to iterate over all records in `calls`, performing constant-time operations for each record to determine if it is a call from Bangalore and if it is a call to Bangalore.

## Task4.py

1. **Appending to `senders` and `receivers` lists:**
   - Let's denote the number of records in `calls` as `N`.
   - For each record in `calls`, the script appends the sender and receiver numbers to the `senders` and `receivers` lists, respectively. Appending to a list in Python is generally an O(1) operation. Thus, for `N` calls, this part is O(N).

2. **Appending to `text_nums` list:**
   - Let's denote the number of records in `texts` as `M`.
   - For each record in `texts`, the script appends both the sender and receiver numbers to the `text_nums` list. Since two numbers are appended for each record, and appending is O(1), this part is O(2M), which simplifies to O(M).

3. **Creating sets and performing set operations:**
   - Conversion of `senders`, `receivers`, and `text_nums` lists to sets. The worst-case time complexity for converting a list of size `k` to a set is O(k), because each element must be hashed and added to the set. Therefore, this step has complexities of O(N), O(N), and O(M), respectively.
   - The set difference operations (`set(senders) - set(receivers) - set(text_nums)`) involve checking each element in the first set against all elements in the second (and third) sets. The worst-case time complexity for set difference is O(n) where `n` is the number of elements in the set. Assuming `senders` has unique `N` elements, `receivers` has unique `N` elements, and `text_nums` has unique `2M` elements, the complexity of this step is O(N + M), as the set difference operation is applied sequentially.

4. **Sorting and printing the suspects:**
   - Sorting the suspects set. The worst-case time complexity of sorting `n` elements is O(n log n). If there are `S` suspects, this step is O(S log S).
   - Printing each suspect number. If there are `S` suspects, and printing each is considered an O(1) operation, this step is O(S).

Combining these steps, the overall worst-case time complexity of the script is dominated by the sorting operation and the list-to-set conversions, leading to **O(N + M + S log S)**. This represents the time to process all records in `calls` and `texts`, perform set operations to identify suspects, sort these suspects, and then print them.