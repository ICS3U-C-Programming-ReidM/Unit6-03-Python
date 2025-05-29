#!/usr/bin/env python3
# Created by: Reid MacLean
# Created on: May 2025
# This program find the minimum value in a list of random numbers between 1 and 100


import random

# Constants
MAX_ARRAY_SIZE = 10
MIN_NUM = 0
MAX_NUM = 100


def find_min_value(numbers):
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val


def main():
    # Generate random numbers
    numbers = []
    for _ in range(MAX_ARRAY_SIZE):
        numbers.append(random.randint(MIN_NUM, MAX_NUM))

    print("Generated numbers:", numbers)

    # Find and display minimum value
    min_value = find_min_value(numbers)
    print("Minimum value:", min_value)


if __name__ == "__main__":
    main()
