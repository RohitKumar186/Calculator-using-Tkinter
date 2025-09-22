# Calculator-using-Tkinter
# Tkinter Calculator

## Overview
This is a simple GUI-based calculator built using Python's Tkinter library. It supports basic arithmetic operations such as addition, subtraction, multiplication, division, and remainder, along with functionalities like backspace, toggle sign (+/-), and decimal input.

## Features
- **Basic Operations:**
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`x`)
  - Division (`/`)
  - Remainder (`%`)
- **Additional Functionalities:**
  - **AC (All Clear):** Clears the current input.
  - **Backspace (`<x`):** Deletes the last character entered.
  - **Toggle Sign (`+/-`):** Changes the sign of the current number.
  - **Decimal Input (`.`):** Allows floating-point calculations.
- **User Interface:**
  - Built using Tkinter.
  - Clean layout with buttons arranged in a standard calculator format.
  - Entry widget shows current input and result.

## How it Works
1. The calculator uses Tkinter’s `Button` and `Entry` widgets to create a functional GUI.
2. Clicking numbers or the decimal appends them to the Entry widget via the `click()` function.
3. Operator buttons store the first operand and the operation type in global variables.
4. The `equal()` function retrieves the second operand, performs the operation, and displays the result.
5. Special functions:
   - **AC:** Clears all input.
   - **Backspace:** Removes the last character.
   - **Toggle Sign:** Switches the number between positive and negative.
6. Supports floating-point numbers using `float()`.
7. Remainder operation uses `int()` to mimic integer modulus behavior.

## Dependencies
- Python 3.x
- Tkinter (built-in with Python)

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/Calculator-using-Tkinter.git
