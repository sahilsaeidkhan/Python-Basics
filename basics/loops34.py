# Question (medium)
# Write a Python function named `find_primes` that takes two integers, `start` and `end`, and
# returns a list of all prime numbers between (and including) `start` and `end`.

# Hint
# Consider using a helper function to check if a number is prime by verifying that it is not
# divisible by any number from 2 up to its square root.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(start, end):
    primes = []
    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)
    return primes

# Example usage
print(find_primes(10, 50))


# Question (medium)
# Write a function in Python that checks if a given string is a palindrome, ignoring spaces,
# punctuation, and capitalization. A palindrome is a word or phrase that reads the same forward
# and backward.
