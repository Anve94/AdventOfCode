"""
A new system policy has been put in place that requires all accounts
to use a passphrase instead of simply a password. A passphrase consists
of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - aa and aaa count as different words.
The system's full passphrase list is available as your puzzle input.
How many passphrases are valid?
"""

with open('4.in', 'r') as infile:
    valid_count = 0
    for line in infile:
        # [:-1] to remove trailing \n
        line = line[:-1]
        words = line.split(" ")
        # Create a new list with solely duplicate words. Phrase is valid
        # if the resulting list is empty.
        if len([word for word in words if words.count(word) > 1]) == 0:
            valid_count += 1

print(valid_count)