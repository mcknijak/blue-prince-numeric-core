# Numeric Core Decoder

This project provides two Python scripts to decode words into letters using a custom **numeric core** algorithm inspired by the roguelite puzzle game **Blue Prince**.

## Overview

The **numeric core** algorithm is a puzzle mechanic from *Blue Prince*, where sequences of numbers are combined using basic arithmetic operations to produce a unique "core" value.

### Numeric Core Algorithm Explained

- Each letter (A-Z) is converted to a number (1-26).
- Words are split into consecutive groups of 4 letters.
- For each group of 4 numbers `[a, b, c, d]`, we apply the three arithmetic operations **subtraction (-), multiplication (*), and division (/)** in every possible order **without rearranging the numbers**.
- The operations are applied sequentially as:  
  `(((a op1 b) op2 c) op3 d)`
- The first number `a` is always the starting value; only the operations' order is permuted.
- The result must be a **whole number between 1 and 26 inclusive** to be valid.
- Among all valid results, the smallest is chosen as the numeric core.
- This numeric core value is then converted back to a letter (1 → A, 2 → B, ..., 26 → Z).
- Decoding each group produces a letter, and concatenating these produces the decoded word.
- Multiple words on a line are decoded and concatenated to produce the final decoded output.

This algorithm is a direct adaptation of the puzzle logic found in *Blue Prince*, a game that blends number puzzles and roguelite elements where players decode sequences using arithmetic operations under constraints.

## Files

- `numeric_core_debug.py` — Outputs detailed intermediate steps showing letter-to-number conversion, groups, operations tried, and results.
- `numeric_core_simple.py` — Outputs only the final decoded letters per input line, for easier use.

## Usage

Run either script with an input filename as argument:

```bash
python numeric_core_debug.py input.txt
python numeric_core_simple.py input.txt
