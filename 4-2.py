"""
For added security, yet another system policy has been put in place.
Now, a valid passphrase must contain no two words that are anagrams
of each other - that is, a passphrase is invalid if any word's letters
can be rearranged to form any other word in the passphrase.

For example:

abcde fghij is a valid passphrase.
abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
iiii oiii ooii oooi oooo is valid.
oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.
Under this new system policy, how many passphrases are valid?
"""

with open('4.in', 'r') as infile:
    valid_count = 0
    for line in infile:
        # [:-1] to remove trailing \n
        line = line[:-1]
        words = line.split(" ")
        # Sort and reorder every word alphabetically
        words = [''.join(sorted(word)) for word in words]
        # Create a new list with solely duplicate words. Phrase is valid
        # if the resulting list is empty.
        if len([word for word in words if words.count(word) > 1]) == 0:
            valid_count += 1

print(valid_count)