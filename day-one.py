import numpy as np

max_val = 0
current_sum = 0
calories = []
with open('input/day-one.inp', 'r') as file:
    for line in file:
        val = line.rstrip()
        if val:
            current_sum += int(val)
        else:
            if current_sum > max_val:
                max_val = current_sum
            calories.append(current_sum)
            current_sum = 0
# Part 1
print(max_val)

# Part 2
calories.sort(reverse=True)
print(sum(calories[0:3]))