"""
--- Part Two ---

Now, the jumps are even stranger: after each jump, 
if the offset was three or more, instead decrease it by 1. 
Otherwise, increase it by 1 as before.

Using this rule with the above example, the process now takes 10 steps, 
and the offset values after finding the exit are left as 2 3 2 3 -1.

How many steps does it now take to reach the exit?
"""

values = []
with open('5.in', 'r') as infile:
    for line in infile:
        values.append(int(line))

cur_pos = 0
jumps = 0
while cur_pos < len(values) and cur_pos >= 0:
    next_pos = values[cur_pos]
    if values[cur_pos] >= 3:
        values[cur_pos] -= 1
    else:
        values[cur_pos] += 1
    jumps += 1
    cur_pos += next_pos
 
print(jumps)