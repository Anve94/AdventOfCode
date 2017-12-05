"""
Continuation of 2-1.
Now, find the two values where a division is possible and add that
division to the checksum instead
"""
import re

def solve_line(values):
    # values is the list of values in the infile line
    for index, v in enumerate(values):
        for i in range(len(values)):
            if index == i:
                continue
            if v % values[i] == 0 or values[i] % v == 0:
                return max(v, values[i]) / min(v, values[i])

checksum = 0

with open('2.in', 'r') as infile:
    for line in infile:
        values = re.split(r'\t+', line)
        values = [int(v) for v in values]
        checksum += solve_line(values)

print(checksum)