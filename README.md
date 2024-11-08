# Collatz Sequence Generator

A Python program to generate the Collatz sequence (also known as the 3n + 1 sequence) for a given starting integer. This project demonstrates fundamental Python concepts, including loops, conditionals, and user input handling.

## Table of Contents

- [About the Project](#about-the-project)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [License](#license)

## About the Project

The Collatz Sequence Generator calculates the Collatz sequence for any positive integer input by the user. The sequence follows these rules:

1. If the number is even, divide it by 2.
2. If the number is odd, multiply it by 3 and add 1.
3. Repeat until the sequence reaches 1.

The Collatz conjecture suggests that every positive integer will eventually reach 1 using this sequence, although it has not been proven mathematically.

## Project Structure

- `main.py`: The main script to start the program, handle user input, and display the generated sequence.
- `collatz.py`: Contains the `collatz_sequence` function, which calculates the Collatz sequence.
- `utils.py`: Contains helper functions for user input validation.
- `README.md`: Project documentation.
- `requirements.txt`: Lists project dependencies and the Python version required.

## Requirements

- **Python**: Version 3.10 or higher

All dependencies are standard Python libraries, so no additional packages are required.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YourUsername/CollatzSequenceProject.git
   cd CollatzSequenceProject
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the program and generate the Collatz sequence, execute:

```bash
python main.py
```

You will be prompted to enter a starting integer greater than 0. The program will then calculate and display the sequence.

## Example

Example interaction with the program:

```
Collatz Sequence, or, the 3n + 1 Problem
By Al Sweigart al@inventwithpython.com

The Collatz sequence is a sequence of numbers produced from a starting
number n, following three rules:

1) If n is even, the next number n is n / 2.
2) If n is odd, the next number n is n * 3 + 1.
3) If n is 1, stop. Otherwise, repeat.

Enter a starting number (greater than 0) or QUIT:
> 6
6, 3, 10, 5, 16, 8, 4, 2, 1
```

## License

This project is open-source and available under the MIT License.
