# <img src="Programs/Python-Light.svg" width="32" height="32"> Python Programming Notes

✨ This README contains simple explanations and definitions of Python concepts covered in my programs. These notes are designed for quick reference during exam preparation. 🚀

> 💡 **Study Tip**: Use these colorful notes to quickly review key Python concepts before exams!

## 📋 Table of Contents
1. 📤 [Basic Output](#-basic-output)
2. 🔠 [Variables and Data Types](#-variables-and-data-types)
3. ⌨️ [User Input](#-user-input)
4. 🧮 [Basic Operators](#-basic-operators)
5. 🔄 [Control Flow](#-control-flow)
6. 📝 [String Formatting](#-string-formatting)
7. 📐 [Mathematical Operations](#-mathematical-operations)
8. 📚 [Study Tips](#-study-tips)

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
- 📦 **tuple**: Ordered collection of items (e.g., (1, 2, 3))
- 🔑 **dict**: Dictionary (key-value pairs)
- 🧩 **set**: Collection of unique items
- ✅ **bool**: Boolean values (True or False)
- ❓ **None**: Represents the absence of a value
- 🏷️ **type**: Returns the type of an object
- ⌨️ **input**: Allows the program to receive input from the user
- 🖨️ **print**: Displays output to the console


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

### 🔢 Python Arithmetic Operators
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

### ✍️ Short Hand Operators
**Definition**: Operators that perform a mathematical operation and assign the result to a variable.

| Operator | Name           | Description                                | Example  | Result |
| -------- | -------------- | ------------------------------------------ | -------- | ------ |
| `+=`     | Addition       | Adds two numbers                           | `5 += 2` | `7`    |
| `-=`     | Subtraction    | Subtracts second number from first         | `5 -= 2` | `3`    |
| `*=`     | Multiplication | Multiplies two numbers                     | `5 *= 2` | `10`   |
| `/=`     | Division       | Divides first number by second             | `5 /= 2` | `2.5`  |
| `//=`    | Floor Division | Division that rounds down to nearest int   | `5 //= 2` | `2`    |
| `%=`     | Modulus        | Returns the remainder                      | `5 %= 2` | `1`    |
| `**=`    | Exponentiation | Raises first number to the power of second | `5 **= 2` | `25`   |


```python
x = 12
y = 15
print(x += y) # 27
print(x -= y) # 12
print(x *= y) # 180
print(x /= y) # 12
print(x //= y) # 1
print(x %= y) # 12
print(x **= y) # 180
```

---

## 🔄 Control Flow

### 🔁 For Loop
**Definition**: A loop that iterates over a sequence (like a list, tuple, or string) or range.

```python
# Loop from 0 to 3
for i in range(4):
    print(i)  # Outputs: 0, 1, 2, 3

# Loop from 50 to 20 with step -10
for i in range(50, 10, -10):
    print(i)  # Outputs: 50, 40, 30, 20
```

---

## 📝 String Formatting

### ⚙️ Print Parameters
**Definition**: Additional parameters in the print function to control output format.

- `sep`: Separator between values (default is space)
- `end`: What to print at the end (default is newline '\n')

```python
print("My", "name", "is", sep="-", end=" ")  # Outputs: My-name-is 
print("My", "name", "is", sep="_", end="*") # Outputs: My_name_is*
```

---

## 📐 Mathematical Operations

### 📏 Area Calculation
**Definition**: Calculating the area of geometric shapes using formulas.

```python
# Area of a circle
pi = 3.14
r = 2
area = pi * r * r
print("Area of Circle is:", round(area, 2))  # Outputs: Area of Circle is: 12.56
```

### 🔄 Variable Swapping
**Definition**: Exchanging values between variables.

```python
# Method 1: Using simultaneous assignment
x = 12
y = 15
x, y = y, x
print(x, y)  # Outputs: 15 12

# Method 2: Using arithmetic operations
x = 18
y = 20
x = x + y  # x = 38
y = x - y  # y = 18
x = x - y  # x = 20
print(x, y)  # Outputs: 20 18
```

---

## 📚 Study Tips

> 🌟 **Remember**: Practice is key to mastering Python!

### 🎯 Quick Review Tips
- 🔍 **Focus on understanding** concepts rather than memorizing code
- 🧠 **Try to write code** without looking at references to test your knowledge
- 🔄 **Review these notes** regularly to reinforce your learning
- ⚡ **Create flashcards** for Python syntax and concepts you find challenging
- 🧪 **Experiment with code** by modifying examples to see what happens

---

<div align="center">

### 🐍 Happy Python Coding! 🐍

*"The only way to learn a programming language is by writing programs in it." - Dennis Ritchie*

</div>