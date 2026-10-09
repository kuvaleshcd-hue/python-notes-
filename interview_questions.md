# Basic Python Interview Questions

## General & Basics
1. **What is Python? What are its key features?**
   - *Answer*: Interpreted, dynamically typed, object-oriented, high-level, easy syntax, extensive standard library.
2. **Is Python an interpreted or compiled language?**
   - *Answer*: Python is both. Source code is compiled into byte code, which is then interpreted by the Python Virtual Machine (PVM).
3. **What is PEP 8?**
   - *Answer*: The style guide for Python code.
4. **How is memory managed in Python?**
   - *Answer*: Private heap space, Python memory manager, and garbage collector - primarily reference counting.
5. **What are the differences between Python 2 and Python 3?**
   - *Answer*: Print as a function, integer division, Unicode strings by default, etc.

## Data Types & Structures
6. **What is the difference between a list and a tuple?**
   - *Answer*: Lists are mutable, tuples are immutable.
7. **What is a dictionary in Python?**
   - *Answer*: An unordered, mutable collection of key-value pairs.
8. **What is a set? How is it different from a list?**
   - *Answer*: An unordered collection of unique elements. Sets do not allow duplicates and don't support indexing.
9. **Explain the difference between mutable and immutable data types.**
   - *Answer*: Mutable objects can be changed after creation (lists, dicts, sets). Immutable objects cannot (strings, ints, tuples).
10. **What is negative indexing?**
    - *Answer*: Using negative numbers to access elements from the end of a sequence, e.g., `list[-1]` gets the last element.
11. **How do you copy an object in Python? (Shallow copy vs. Deep copy)**
    - *Answer*: Using `copy` module. Shallow copy creates a new object but inserts references into it. Deep copy recursively copies objects.

## Control Flow & Functions
12. **What is the difference between `break`, `continue`, and `pass`?**
    - *Answer*: `break` exits a loop, `continue` skips the rest of the current iteration, `pass` is a null operation/placeholder.
13. **What are `*args` and `**kwargs`?**
    - *Answer*: `*args` allows passing a variable number of positional arguments. `**kwargs` allows passing a variable number of keyword/named arguments.
14. **What is a lambda function?**
    - *Answer*: An anonymous, single-expression function created using the `lambda` keyword.
15. **What is a generator in Python?**
    - *Answer*: A function that returns an iterator using the `yield` keyword instead of `return`, evaluating values lazily.
16. **What is a decorator?**
    - *Answer*: A function that takes another function and extends its behavior without explicitly modifying it.

## Object-Oriented Programming (OOP)
17. **What is `__init__`?**
    - *Answer*: The constructor method in Python classes, called when an object is instantiated.
18. **What is the `self` keyword?**
    - *Answer*: It represents the instance of the class and is used to access variables and methods associated with that instance.
19. **What are magic methods (dunder methods)?**
    - *Answer*: Methods with double underscores like `__str__`, `__len__`, `__add__` that allow overriding default Python behaviors.
20. **Does Python support multiple inheritance?**
    - *Answer*: Yes. A class can inherit from multiple parent classes.

## Built-in Functions & Modules
21. **What is the purpose of `is` vs `==`?**
    - *Answer*: `==` checks for value equality. `is` checks for object identity/memory location.
22. **What does the `map()`, `filter()`, and `reduce()` functions do?**
    - *Answer*: `map` applies a function to all items, `filter` filters items based on a function, `reduce` applies a rolling computation to sequential pairs of values in a list.
23. **What is a virtual environment in Python?**
    - *Answer*: An isolated environment for Python projects to manage dependencies separately.
24. **How do you handle exceptions in Python?**
    - *Answer*: Using `try`, `except`, `else`, and `finally` blocks.
25. **What does `if __name__ == "__main__":` do?**
    - *Answer*: It ensures that the block of code inside it runs only if the script is executed directly, not if it's imported as a module.

## Common Basic Coding Questions
- **Reverse a String**
- **Check if a string is a Palindrome**
- **Find the Factorial of a number** (Iterative and Recursive)
- **Check if a number is Prime**
- **Generate the Fibonacci sequence**
- **Swap two numbers without a temporary variable**
- **Implement Binary Search**
