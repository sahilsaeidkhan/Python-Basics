print("This is my first python code ( Date - 3 October)")

# Question (medium)
# Create a function `expand_range` that takes a string representing a range in the format "1-5"
# and returns a list of numbers in this range inclusive of both endpoints. The function should
# also handle single numbers correctly and return them in a list.

# Question Explanation
# The task is to create a function named `expand_range` that does the following:
# 1. It receives a string that looks like "1-5" or just "3".
# 2. If the string is a range like "1-5", the function should return a list of all numbers from 1
# to 5, including both 1 and 5.
# 3. If the string is just a single number like "3", the function should return a list containing
# just that number, [3].
# This function should be able to understand and convert both types of inputs into a list of
# numbers.

def expand_range(range_str):
    if '-' in range_str:
        start, end = map(int, range_str.split('-'))
        return list(range(start, end + 1))
    else:
        return [int(range_str)]

# Example of function execution
print(expand_range("1-5"))
print(expand_range("3"))
