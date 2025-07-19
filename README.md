# <img src="Programs/Python-Light.svg" width="32" height="32"> Python Programming Notes

✨ Concise explanations and definitions of Python concepts for quick exam reference. 🚀

> 💡 **Study Tip**: These notes cover essential Python concepts with clear examples for efficient exam preparation!

## 📋 Table of Contents
1. 📤 [Basic Output](#-basic-output)
2. 🔠 [Variables and Data Types](#-variables-and-data-types)
3. ⌨️ [User Input](#-user-input)
4. 🧮 [Basic Operators](#-basic-operators)
5. 🔄 [Control Flow](#-control-flow)


---

## 📤 Basic Output

### 🖨️ Print Function
**Definition**: The `print()` function displays output to the console.

```python
print("Hello World!")  # Outputs: Hello World!
```

---

## 🔠 Variables and Data Types

### 📦 Variables
**Definition**: Variables are containers for storing data values.

```python
x = 10        # Integer variable
name = "John"  # String variable
```

### 🏷️ Data Types
**Definition**: Data types categorize the type of data a variable can hold.

#### 📊 Common Data Types:
- 🔢 **int**: Integer values (e.g., 5, -3, 42)
- 🔣 **float**: Decimal values (e.g., 3.14, -0.001, 2.0)
- 📝 **str**: Text strings (e.g., "Hello", 'Python')
- 📋 **list**: Ordered collection of items (e.g., [1, 2, 3])
- 📦 **tuple**: Ordered, immutable collection (e.g., (1, 2, 3))
- 🔑 **dict**: Dictionary with key-value pairs (e.g., {'key': 'value'})
- 🧩 **set**: Collection of unique items (e.g., {1, 2, 3})
- ✅ **bool**: Boolean values (True or False)
- ❓ **None**: Represents the absence of a value


```python
x = 10
print(type(x))  # Outputs: <class 'int'>

y = 10.21
print(type(y))  # Outputs: <class 'float'>

z = "Krutarth"
print(type(z))  # Outputs: <class 'str'>
```

---

## ⌨️ User Input

### 📥 Input Function
**Definition**: The `input()` function allows the program to receive input from the user.

```python
user = input("Enter your name: ")
print("Hello", user, "!")
```

### 🔄 Type Conversion
**Definition**: Converting input data from one type to another.

```python
x = int(input("Enter a number: "))  # Converts input string to integer
y = float(input("Enter a number: "))  # Converts input string to float
z = str(input("Enter a number: "))  # Converts input string to string

print(type(x))  # Outputs: <class 'int'>
print(type(y))  # Outputs: <class 'float'>
print(type(z))  # Outputs: <class 'str'>

```

---

## 🧮 Basic Operators

### 1.🔢 Python Arithmetic Operators
**Definition**: Operators used to perform mathematical operations. which contain 1 operator and 2 operands.

| Operator | Name           | Description                                | Example  | Result |
| -------- | -------------- | ------------------------------------------ | -------- | ------ |
| `+`      | Addition       | Adds two numbers                           | `5 + 2`  | `7`    |
| `-`      | Subtraction    | Subtracts second number from first         | `5 - 2`  | `3`    |
| `*`      | Multiplication | Multiplies two numbers                     | `5 * 2`  | `10`   |
| `/`      | Division       | Divides first number by second             | `5 / 2`  | `2.5`  |
| `//`     | Floor Division | Division that rounds down to nearest int   | `5 // 2` | `2`    |
| `%`      | Modulus        | Returns the remainder                      | `5 % 2`  | `1`    |
| `**`     | Exponentiation | Raises first number to the power of second | `5 ** 2` | `25`   |

### Example Code:

```python
# Addition
print(10 + 4)      # 14

# Subtraction
print(10 - 4)      # 6

# Multiplication
print(10 * 4)      # 40

# Division
print(10 / 4)      # 2.5

# Floor Division
print(10 // 4)     # 2

# Modulus
print(10 % 4)      # 2

# Exponentiation
print(2 ** 4)      # 16

# Unary operators
x = 5
print(-x)          # -5
print(+x)          # 5
```

### 2.✍️ Assignment (Short Hand) Operators
**Definition**: Operators that perform a mathematical operation and assign the result to a variable.

| Operator | Name           | Description                                | Example  | Result |
| -------- | -------------- | ------------------------------------------ | -------- | ------ |
| `=`      | Assignment     | Assigns value to variable                  | `x = 5`  | `5`    |
| `+=`     | Addition       | Adds and assigns                           | `x += 2` | `7`    |
| `-=`     | Subtraction    | Subtracts and assigns                      | `x -= 2` | `3`    |
| `*=`     | Multiplication | Multiplies and assigns                     | `x *= 2` | `10`   |
| `/=`     | Division       | Divides and assigns                        | `x /= 2` | `2.5`  |
| `//=`    | Floor Division | Floor divides and assigns                  | `x //= 2`| `2`    |
| `%=`     | Modulus        | Modulus and assigns                        | `x %= 2` | `1`    |
| `**=`    | Exponentiation | Exponentiates and assigns                  | `x **= 2`| `25`   |


```python
x = 12
y = 15
x += y
print(x)  # 27
x = 12    # Reset x
x -= y
print(x)  # -3
x = 12    # Reset x
x *= y
print(x)  # 180
x = 12    # Reset x
x /= y
print(x)  # 0.8
x = 12    # Reset x
x //= y
print(x)  # 0
x = 12    # Reset x
x %= y
print(x)  # 12
x = 12    # Reset x
x **= y
print(x)  # Very large number
```

### 3.⚖️ Comparison (Relational) Operators
**Definition**: Operators that compare two values and return a boolean result.

| Operator | Description      | Example  |
| -------- | ---------------- | -------- |
| `==`     | Equal to         | `a == b` |
| `!=`     | Not equal to     | `a != b` |
| `>`      | Greater than     | `a > b`  |
| `<`      | Less than        | `a < b`  |
| `>=`     | Greater or equal | `a >= b` |
| `<=`     | Less or equal    | `a <= b` |


### Example Code:

```python
# Equal
print(10 == 4)      # False

# Not Equal
print(10 != 4)      # True

# Greater Than
print(10 > 4)       # True

# Less Than
print(10 < 4)       # False

# Greater or Equal
print(10 >= 4)      # True

# Less or Equal
print(10 <= 4)      # False

```

### 4.🧠 Logical Operators

**Definition**: Operators that combine multiple conditions.

| Operator | Description      | Example  |
| -------- | ---------------- | -------- |
| `and`    | Logical AND      | `a and b` |
| `or`     | Logical OR       | `a or b`  |
| `not`    | Logical NOT      | `not a`   |


### Example Code:

```python
# Logical AND
print(10 > 4 and 10 < 20)  # True

# Logical OR
print(10 > 4 or 10 < 20)   # True

# Logical NOT
print(not 10 > 4)           # False
```



### 5.🧱 Bitwise Operators
**Definition**: Operators that perform bitwise operations on integers.

| Operator | Description         | Example  |
| -------- | ------------------- | -------- |
| `&`      | Bitwise AND         | `a & b`  |
| `|`     | Bitwise OR          | `a \| b`  |
| `^`      | Bitwise XOR         | `a ^ b`  |
| `~`      | Bitwise NOT         | `~a`     |
| `<<`     | Bitwise Left Shift  | `a << 2` |
| `>>`     | Bitwise Right Shift | `a >> 2` |

### Example Code:

```python
# Bitwise AND
print(10 & 4)  # 4

# Bitwise OR
print(10 | 4)  # 14

# Bitwise XOR
print(10 ^ 4)  # 12

# Bitwise NOT
print(~10)  # -11

# Bitwise Left Shift
print(10 << 2)  # 40

# Bitwise Right Shift
print(10 >> 2)  # 2
```

### 6.🧩 Unary Operators
**Definition**: Operators that work on a single operand.

| Operator | Description         | Example  |
| -------- | ------------------- | -------- |
| `+`      | Positive            | `+a`     |
| `-`      | Negative            | `-a`     |
| `~`      | Bitwise NOT         | `~a`     |

### Example Code:

```python
# Positive
print(+10)  # 10

# Negative
print(-10)  # -10

# Bitwise NOT
print(~10)  # -11
```

### 7.🧪 Ternary Operator
**Definition**: A shorthand way to write simple if-else statements.

Syntax:
```
value = true_value if condition else false_value
```

```python
# Simple if-else statement
x = 10
result = "Positive" if x > 0 else "Negative"
print(result)  # Outputs: Positive

# Nested ternary operator
x = 10
result = "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(result)  # Outputs: Positive
```


---

## 🔄 Control Flow

### 🔁 For Loop
**Definition**: A loop that iterates over a sequence (like a list, tuple, or string) or range.

Syntax :
```
for item in sequence:
    # Do something with item
```

```python
# Loop from 0 to 3
for i in range(4):
    print(i)  # Outputs: 0, 1, 2, 3

# Loop from 50 to 20 with step -10
for i in range(50, 10, -10):
    print(i)  # Outputs: 50, 40, 30, 20
```

### 🔀 While Loop
**Definition**: A loop that executes as long as a condition is true.

Syntax :
```
while condition:
    # Do something
```

```python
# Count from 0 to 3
i = 0
while i < 4:
    print(i)  # Outputs: 0, 1, 2, 3
    i += 1
```
---

<div align="center">

### 🐍 Happy Python Coding! 🐍

*"The only way to learn a programming language is by writing programs in it." - Dennis Ritchie*

</div>