"""This module provides a function to generate the Collatz sequence
(also known as the 3n + 1 sequence), starting from a specified integer.
The Collatz conjecture suggests that, given any positive integer,
the sequence will always reach 1."""


def collatz_sequence(start):
    """Generate the Collatz sequence starting from the given integer."""
    sequence = [start]
    while start != 1:
        start = start // 2 if start % 2 == 0 else 3 * start + 1
        sequence.append(start)
    return sequence
