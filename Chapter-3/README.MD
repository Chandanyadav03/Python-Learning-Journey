# Chapter 3 - Strings

## Topics Learned

### 1. Strings

A string is a sequence of characters enclosed in single quotes, double quotes, or triple quotes.

Example:

```python
name = "Vipul"
message = 'Hello'
```

### 2. String Indexing

Each character in a string has an index position.

Example:

```python
name = "Python"

print(name[0])  # P
print(name[1])  # y
```

### 3. String Slicing

String slicing is used to extract a portion of a string.

Example:

```python
name = "Python"

print(name[0:3])   # Pyt
print(name[1:4])   # yth
```

### 4. Types of Slicing

#### Positive Slicing

```python
name = "Python"
print(name[0:4])   # Pyth
```

#### Negative Slicing

```python
name = "Python"
print(name[-4:-1]) # tho
```

#### Skip Value Slicing

```python
name = "Python"
print(name[0:6:2]) # Pto
```

#### Slicing from Start

```python
name = "Python"
print(name[:4])    # Pyth
```

#### Slicing to End

```python
name = "Python"
print(name[2:])    # thon
```

### 5. String Functions

Common string methods:

```python
name = "python"

print(len(name))
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.replace("python", "Python"))
```
### Escape Sequence Characters

```python
\n   # New Line
\t   # Tab
\\   # Backslash
\'   # Single Quote
\"   # Double Quote

## What I Learned

* What is a string
* String indexing
* Positive slicing
* Negative slicing
* Skip value slicing
* String methods and functions
* String manipulation basics



## Practice Set

1. Write a Python program to display a user-entered name followed by **"Good Afternoon"** using the `input()` function.

2. Write a program to fill in a letter template given below with a name and date.

```python
letter = '''
Dear <|Name|>,

You are selected!

<|Date|>
'''

### Question 3
Write a Python program to detect double spaces in a string.

### Question 4
Write a Python program to replace the double spaces found in Question 3 with single spaces.

### Question 5
Write a Python program to format the following letter using escape sequence characters.

```python
letter = "Dear Harry, this python course is nice. Thanks!"
```