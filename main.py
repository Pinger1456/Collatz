"""This script launches the Collatz Sequence program,
which generates and displays the Collatz sequence (or 3n + 1 sequence)
for a given starting integer.
The sequence follows these rules:

1. If the number is even, divide it by 2.
2. If the number is odd, multiply it by 3 and add 1.
3. Repeat until the sequence reaches 1."""

from collatzzz.collatz import collatz_sequence
from utils import get_starting_number


def main():
    """Main function to run the Collatz Sequence program."""
    print('''Collatz Sequence, or, the 3n + 1 Problem
By Al Sweigart al@inventwithpython.com

The Collatz sequence is a sequence of numbers produced from a starting
number n, following three rules:

1) If n is even, the next number n is n / 2.
2) If n is odd, the next number n is n * 3 + 1.
3) If n is 1, stop. Otherwise, repeat.

It is generally thought, but so far not mathematically proven, that
every starting number eventually terminates at 1.
''')

    # Получаем начальное число
    n = get_starting_number()

    # Генерируем последовательность
    sequence = collatz_sequence(n)

    # Выводим последовательность
    print(', '.join(map(str, sequence)))


# Запуск main() при прямом вызове файла
if __name__ == "__main__":
    main()
