## Task0.py

1. **Reading the files (`texts.csv` and `calls.csv`):** The time complexity of reading a file is $O(N)$, where $N$ is the number of lines in the file. This is because each line must be read and processed. Since there are two files, if we assume `texts.csv` has $N$ lines and `calls.csv` has $M$ lines, the complexity for this part is $O(N + M)$.

2. **Converting the file contents to lists:** The `list(reader)` operation converts the iterable returned by `csv.reader` into a list. This operation is also $O(N)$ for each file, as it must iterate through each item produced by the reader. Thus, for both files together, this remains $O(N + M)$.

3. **Accessing the first and last records of the lists:** Accessing an element in a list by index is an $O(1)$ operation. Therefore, accessing the first record of `texts` and the last record of `calls` does not significantly add to the overall time complexity.

4. **Printing the records:** The time complexity of printing is generally considered $O(1)$ for a fixed-size output, which is the case here. However, it's worth noting that the actual time taken can vary based on the environment and is generally not considered in algorithmic complexity analysis.

Combining these, the overall worst-case time complexity of the script is dominated by the file reading and list conversion steps, leading to a final complexity of $O(N + M)$, where $N$ is the number of records in `texts.csv` and $M$ is the number of records in `calls.csv`.

## Task1.py

1. **Initialization of a set (`telephones`):** This is an $O(1)$ operation, as it simply initializes an empty set.

2. **Iterating over `texts` and `calls` records and adding telephone numbers to the set:** 
   - The `for` loop iterates over each record in `texts` and `calls`. Let's denote the number of records in `texts` as `N` and in `calls` as `M`.
   - For each iteration, two `add` operations are performed – one for each telephone number in the record (sender and receiver). The `add` operation for a set in Python is generally $O(1)$, assuming a good hash function and that the hash table does not need to be resized too often. However, in the worst case (e.g., when a resize occurs), it could temporarily be $O(n)$, but this is rare and amortized over many additions to be considered $O(1)$ for each addition.
   - Therefore, for both loops combined, if we consider the `add` operation as $O(1)$ in average case, the total complexity for this part is $O(N + M)$.

3. **Calculating the length of the set and printing the result:** 
   - The `len` function is $O(1)$ as it simply returns the count of elements in the set, which is maintained with the set's metadata.
   - The `print` function's complexity is not typically considered in algorithmic complexity analysis, as it is dependent on the environment and is generally $O(1)$ for practical purposes.

Combining these, the overall worst-case time complexity of the script is dominated by the loops that iterate over `texts` and `calls`, leading to a final complexity of $O(N + M)$. This represents the time to iterate over all records in both `texts` and `calls` and add their telephone numbers to the set, where $N$ is the number of records in `texts` and $M$ is the number of records in `calls`.

## Task2.py

1. **Initialization of a defaultdict (`duration`):** This is an $O(1)$ operation, as it simply initializes an empty defaultdict with integers.

2. **Iterating over `calls` records and updating `duration`:**
   - Let's denote the number of records in `calls` as $N$.
   - The loop iterates over each record in `calls`. For each iteration, it performs two update operations on the `duration` defaultdict.
   - Updating the defaultdict for a key (either adding a new key or updating an existing one) is generally considered an $O(1)$ operation, assuming a good hash function and that the hash table does not need to be resized too often. However, in the worst case (e.g., when a resize occurs), it could temporarily be $O(n)$, but this is rare and amortized over many additions to be considered $O(1)$ for each addition.
   - Therefore, for the loop, the total complexity is $O(2N) = O(N)$, as each record involves two $O(1)$ operations.

3. **Finding the maximum duration:**
   - The `max` function with a key argument iterates over each item in `duration.items()`, which in this case, will be $N$ items if all calls are between unique pairs, or fewer if some numbers are repeated.
   - The iteration itself is $O(N)$, as it needs to check each item once to determine the maximum.
   - The lambda function provided to the `key` argument is $O(1)$ for each item, as it simply returns the value part of the tuple.

4. **Printing the result:** The complexity of the `print` function is not typically considered in algorithmic complexity analysis, as it is dependent on the environment and is generally $O(1)$ for practical purposes.

Combining these steps, the overall worst-case time complexity of the script is $O(N)$. This represents the time to iterate over all records in `calls`, update the `duration` for each number, and then find the number with the maximum duration.

## Task3.py

### Part A: Finding Area Codes and Mobile Prefixes

1. **Iterating over `calls` records:**
   - Let's denote the number of records in `calls` as $N$.
   - The loop iterates over each record in `calls`. The worst-case time complexity for this loop is $O(N)$ because it examines each call record.

2. **Checking if the call is from Bangalore and extracting codes:**
   - The check for whether a call is from Bangalore (`record[0].startswith("(080)")`) is an $O(1)$ operation because it compares a fixed number of characters at the start of the string.
   - Extracting codes involves:
     - Checking the first character of the called number to identify mobile numbers, which is $O(1)$.
     - Finding the closing parenthesis for fixed lines, which is $O(k)$ in the worst case, where $k$ is the length of the phone number. However, since $k$ is relatively small and constant, this can be considered $O(1)$ for practical purposes.
     - Adding the extracted code to a set, which is generally $O(1)$ on average due to hash table operations, but can be worse in cases of hash collisions.

3. **Sorting and printing the codes:**
   - Converting the set of codes to a list and sorting it has a complexity of $O(C \log C)$, where $C$ is the number of unique codes.
   - Printing each code is $O(C)$, assuming printing each code is an $O(1)$ operation.

### Part B: Calculating Percentage of Calls

1. **Iterating over `calls` records again:**
   - This is another loop over $N$ records, so its time complexity is $O(N)$.

2. **Counting calls from and to Bangalore:**
   - The checks and increments inside the loop are $O(1)$ operations.

3. **Calculating and printing the percentage:**
   - The division and printing are $O(1)$ operations.

### Overall Complexity

- **Part A:** The dominant factor is the sorting of codes, making its complexity $O(N + C \log C)$.
- **Part B:** The loop over $N$ records dominates, making its complexity $O(N)$.

Combining both parts, the overall worst-case time complexity of the script is $O(N + C \log C)$. This accounts for iterating over all call records, extracting and sorting unique codes, and calculating the percentage of calls from Bangalore to Bangalore.

## Task4.py

1. **Appending to `senders` and `receivers` lists:**
   - Let's denote the number of records in `calls` as $N$.
   - For each record in `calls`, the script appends the sender and receiver numbers to the `senders` and `receivers` lists, respectively. Appending to a list in Python is generally an $O(1)$ operation. Thus, for $N$ calls, this part is $O(N)$.

2. **Appending to `text_nums` list:**
   - Let's denote the number of records in `texts` as $M$.
   - For each record in `texts`, the script appends both the sender and receiver numbers to the `text_nums` list. Since two numbers are appended for each record, and appending is $O(1)$, this part is $O(2M)$, which simplifies to $O(M)$.

3. **Creating sets and performing set operations:**
   - Conversion of `senders`, `receivers`, and `text_nums` lists to sets. The worst-case time complexity for converting a list of size $k$ to a set is $O(k)$, because each element must be hashed and added to the set. Therefore, this step has complexities of $O(N)$, $O(N)$, and $O(M)$, respectively.
   - The set difference operations (`set(senders) - set(receivers) - set(text_nums)`) involve checking each element in the first set against all elements in the second (and third) sets. The worst-case time complexity for set difference is $O(n)$ where $n$ is the number of elements in the set. Assuming `senders` has unique $N$ elements, `receivers` has unique $N$ elements, and `text_nums` has unique $2M$ elements, the complexity of this step is $O(N + M)$, as the set difference operation is applied sequentially.

4. **Sorting and printing the suspects:**
   - Sorting the suspects set. The worst-case time complexity of sorting $n$ elements is $O(n \log n)$. If there are $S$ suspects, this step is $O(S \log S)$.
   - Printing each suspect number. If there are `S` suspects, and printing each is considered an $O(1)$ operation, this step is $O(S)$.

Combining these steps, the overall worst-case time complexity of the script is dominated by the sorting operation and the list-to-set conversions, leading to $O(N + M + S \log S)$. This represents the time to process all records in `calls` and `texts`, perform set operations to identify suspects, sort these suspects, and then print them.