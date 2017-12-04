""" Assignment
Continuation of 1-1. Now, the next digit to check for is halfway
through the round trip (half the length of the string)
instead of the next one. All inputs have an even number of digits.
"""
def solve(s):
    total = 0
    # Save the length of the original string
    s_length = len(s)
    # The amount of positions to check for the next digit
    round_trip = int(s_length / 2)
    # Append the first half of the string to itself
    s += s[0:round_trip]

    for i, c in enumerate(s):
        # Return if the next character would be out of bounds
        if i + 1 > s_length:
            return total

        if c == s[i+round_trip]:
            total += int(c)

if __name__ == "__main__":
    with open("1.in", 'r') as f:
        inp = f.readline()
    print(solve(inp))