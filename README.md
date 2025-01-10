# Uncommon ZeroDivisionError in Python Conditional
This repository demonstrates a subtle error in Python code involving a `ZeroDivisionError` within a conditional statement.  Even though an `else` block exists, the error can still occur due to the order of conditions being checked.

## The Bug
The `bug.py` file contains a function that attempts to handle division by zero. However, due to the sequence in which the conditional statements are evaluated, the error still occurs even when the `else` condition should logically prevent it.

## The Solution
The `bugSolution.py` provides a corrected version of the function. It ensures that the conditions are evaluated safely to avoid the `ZeroDivisionError`.