# Chapter 1 - Python Basics
-----------------------------------------
## Topics Covered

### 1. Comments
Comments are used to explain code. Python ignores comments during execution.

Example:
```python
# This is a single-line comment
print("Hello World")
```

### 2. Modules
A module is a file containing Python code that can be reused in another program.

Example:
```python
import math

print(math.sqrt(25))
```

Common Modules:
- math
- random
- os
- datetime

### 3. PIP
PIP (Package Installer for Python) is used to install external Python packages.

Commands:

```bash
pip install numpy
pip install pandas
pip install requests
```

Check installed packages:

```bash
pip list
```

Check pip version:

```bash
pip --version
```

## What I Learned
- How to write comments in Python.
- How to use built-in modules.
- How to install packages using pip.

## Example Program

```python
# Using a module

import math

num = 16
print("Square Root:", math.sqrt(num))
```


# Chapter 1 – Practice Set

## Questions

1. Write a program to print the **Twinkle Twinkle Little Star** poem in Python.

2. Use **REPL** and print the table of **5** using it.

3. Install an external module and use it to perform an operation of your interest.

4. Write a Python program to print the contents of a directory using the **os** module.
   - Search online for the function that performs this task.

5. Label the program written in Question 4 with comments.