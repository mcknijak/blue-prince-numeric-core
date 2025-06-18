#!/usr/bin/env python3
"""
numeric_core_simple.py

Simplified version of numeric core decoding:
- Reads lines from a file (filename given on command line)
- Converts words letter-by-letter to numbers
- Computes numeric cores for every group of 4 letters in each word
- Outputs decoded words combined per input line
- No intermediate debug output, just decoded result

Usage:
    python numericCore.py input.txt
"""

import sys
import itertools

def letter_to_number(c):
    """Convert a letter (A-Z) to number (1-26)."""
    return ord(c.upper()) - ord('A') + 1

def apply_ops(a, b, c, d, ops):
    """
    Apply operations ('-', '*', '/') in order on four numbers (a,b,c,d).
    Use float math internally; final result must be integer 1-26 inclusive.
    Returns integer result or None if invalid.
    """
    try:
        result = float(a)
        for val, op in zip((b, c, d), ops):
            val = float(val)
            if op == '-':
                result -= val
            elif op == '*':
                result *= val
            elif op == '/':
                if val == 0:
                    return None
                result /= val
        if result.is_integer() and 1 <= int(result) <= 26:
            return int(result)
        return None
    except Exception:
        return None

def numeric_core(numbers):
    """
    Find minimal numeric core applying permutations of '-', '*', '/'.
    Returns the smallest valid result or None.
    """
    a, b, c, d = numbers
    best = None
    for ops in itertools.permutations(['-', '*', '/'], 3):
        res = apply_ops(a, b, c, d, ops)
        if res is not None and (best is None or res < best):
            best = res
    return best

def number_to_letter(n):
    """Convert number 1-26 to letter A-Z."""
    return chr(ord('A') + n - 1)

def process_word(word):
    """
    Process word by groups of 4 letters to numeric cores and letters.
    Returns decoded word string.
    """
    nums = [letter_to_number(c) for c in word if c.isalpha()]
    letters = []
    for i in range(0, len(nums) - 3, 4):
        group = nums[i:i+4]
        core = numeric_core(group)
        letters.append(number_to_letter(core) if core else '?')
    return ''.join(letters)

def process_line(line):
    """Process a line and print decoded combined words."""
    words = line.strip().split()
    decoded_line = ''.join(process_word(word) for word in words)
    print(decoded_line)

def main():
    """Main function to process file from command line."""
    if len(sys.argv) != 2:
        print("Usage: python numeric_core_simple.py inputfile.txt")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename, 'r') as f:
        for line in f:
            process_line(line)

if __name__ == "__main__":
    main()
