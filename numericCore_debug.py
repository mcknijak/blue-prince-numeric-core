#!/usr/bin/env python3
"""
numeric_core_debug.py

A script that reads lines of text from a file (provided as a command-line argument),
processes each word by converting its letters to numbers (A=1, ..., Z=26),
and computes a "numeric core" from groups of 4 letters using
a permutation of three operations (-, *, /) applied in order.

The script prints detailed debugging information including:
- Letter-to-number conversion
- Each group of 4 letters being processed
- Which operations produced the smallest valid numeric core
- The decoded letter corresponding to the numeric core

Usage:
    python numeric_core_debug.py input.txt
"""

import sys
import itertools

def letter_to_number(c):
    """
    Convert a letter (A-Z) to its corresponding number (1-26).
    """
    return ord(c.upper()) - ord('A') + 1

def apply_ops(a, b, c, d, ops):
    """
    Apply a sequence of operations (ops) to four numbers (a,b,c,d).
    Operations are applied in order: (((a op1 b) op2 c) op3 d).
    
    Allowed operations: '-', '*', '/'
    Division is floating point internally, but final result
    must be an integer between 1 and 26 inclusive.

    Return the resulting integer if valid, else None.
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
        # Validate final result is whole number in valid range
        if result.is_integer() and 1 <= int(result) <= 26:
            return int(result)
        return None
    except Exception:
        return None

def numeric_core(numbers):
    """
    Find the smallest valid numeric core from all permutations
    of the operations '-', '*', '/' applied in order on the numbers.
    Returns a tuple (best_result, best_ops) or (None, None) if none valid.
    """
    a, b, c, d = numbers
    best = None
    best_ops = None
    for ops in itertools.permutations(['-', '*', '/'], 3):
        res = apply_ops(a, b, c, d, ops)
        if res is not None and (best is None or res < best):
            best = res
            best_ops = ops
    if best is not None:
        print(f"    → Best ops: {best_ops} → Result: {best}")
    else:
        print("    → No valid core found")
    return best

def number_to_letter(n):
    """
    Convert a number 1-26 back to uppercase letter A-Z.
    """
    return chr(ord('A') + n - 1)

def process_word(word):
    """
    Process a word:
    - Convert each letter to number
    - For each consecutive group of 4 letters, compute numeric core
    - Convert numeric core to a letter
    Returns the decoded string for the word.
    """
    print(f"Processing word: {word}")
    nums = [letter_to_number(c) for c in word if c.isalpha()]
    print(f" Letter-to-number conversion: {nums}")
    letters = []
    for i in range(0, len(nums) - 3, 4):
        group = nums[i:i+4]
        print(f"  Group of 4: {group}")
        core = numeric_core(group)
        if core is not None:
            letter = number_to_letter(core)
            print(f"    → Numeric Core: {core} → Letter: {letter}")
            letters.append(letter)
        else:
            print(f"    → Numeric Core: None → Letter: ?")
            letters.append('?')
    return ''.join(letters)

def process_line(line):
    """
    Process a line of text by decoding each word and printing
    the combined decoded result.
    """
    words = line.strip().split()
    decoded_words = []
    for word in words:
        decoded_word = process_word(word)
        decoded_words.append(decoded_word)
    decoded_line = ''.join(decoded_words)
    print(f"Decoded line: {decoded_line}\n")

def main():
    """
    Entry point: 
    - Validate command-line argument
    - Read file line-by-line and decode
    """
    if len(sys.argv) != 2:
        print("Usage: python numeric_core_debug.py inputfile.txt")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename, 'r') as f:
        for line in f:
            process_line(line)

if __name__ == "__main__":
    main()
