"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

senders = []
receivers = []

for record in calls:
    senders.append(record[0])
    receivers.append(record[1])

text_nums = []

for record in texts:
    text_nums.append(record[0])
    text_nums.append(record[1])

suspects = set(senders) - set(receivers) - set(text_nums)

print("These numbers could be telemarketers: ")
for num in sorted(list(suspects)):
    print(num)
