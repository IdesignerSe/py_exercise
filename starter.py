""" This is a simple Python script 

print("Hello, World!")

x = 10 
print(x)

y = 10.5
print(y)


Z = x + y  # 20.5
print(Z)

x = "nu är " + "en sträng"
print(x)

# Basic Variable Assignment 
city = "New York"
print("I Love " + city)

# Integer and Float Variables

length = 45
width = 20.5
area = length * width
print("Area of rectangle: " + str(area))

# Type Conversion

num = 100
result = str(num) + " is now a string"
print(result)

 # Boolean Variable - with a slight change in the code
is_open = False
import random 
is_open = random.choice([True, False])
print("Is the store open? " + str(is_open))

# Arithmetic Operations
buy_price = 50
sell_price = 75
profit = sell_price - buy_price
print("Profit: " + str(profit))

# Division and Modulus
dividend = 20
divisor = 3
quotient = dividend // divisor
remainder = dividend % divisor
print("Quotient: " + str(quotient))
print("Remainder: " + str(remainder))

# Exponentiation 
base = 4
exponente = 3

resultado = base ** exponente
print("Potencia:", resultado)

# Example 2
a = 17
b = 5

resto = a % b
print("Resto:", resto)

# Logical AND
x = True
y = False
z = x and y
print("Logical AND:", z)

#  Logical OR
resultado = a or b
print(resultado)

# Comparison Operators
x = 15
y = 25

print(x == y)   # Igual
print(x != y)   # Diferente
print(x > y)    # Mayor que
print(x < y)    # Menor que
print(x >= y)   # Mayor o igual
print(x <= y)   # Menor o igual


# Type Checking
price = 49.99
print(type(price))

#  String Length
word = "Python"
print(len(word))

#  String to Float Conversion
height_str = "180.5"
height = float(height_str)
print(height)

#  Boolean Conversion
zero = 0
non_zero = 5

print(bool(zero))
print(bool(non_zero))

# Declaring an integer variable 
age = 25 
print(age)  # Output: 25

# Declaring a floating-point variable 
price = 19.99 
print(price)  # Output: 19.99  

# Declaring a string variable 
name = "Alice" 
print(name)  # Output: Alice 

# Declaring a boolean variable 
is_student = True 
print(is_student)  # Output: True

# Converting between types 
num = 10 
print(float(num))  # Output: 10.0 

 
text = "123" 
print(int(text))  # Output: 123 


value = 0 
print(bool(value))  # Output: False

my_list = []
print(type(my_list))
my_list.append("Saludos")
my_list.append("a todos")
my_list.append("los estudiantes")
my_list.append(100)
my_list.append(3.14)
my_list.append(True)
print(my_list.append(type(100)))
print(my_list)

my_list_1 = my_list [:]
my_list_1 = my_list [0:4]
my_list_1 = my_list [0:4:2]
my_list_1 = my_list [::2]
my_list_1 = my_list [::-1]

print(my_list_1)

"""

""" 
# 1. Temperature Check 
temp = 28

if temp > 30:
    print("Hot")
elif 20 <= temp <= 30:
    print("Warm")
else:
    print("Cold")


# 2. Even or Odd 
num = 7

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#3. Leap Year Check
year = 2024

if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")

# 4. Age Group
age = 17

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# 5. Positive, Negative, or Zero

number = -5
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# 6. For Loop: Sum of Numbers (1 to 10)
total = 0
for i in range(1, 11):
    total += i      

print("Sum of numbers from 1 to 10:", total)

# 7. For Loop: Multiplication Table of 5
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}") 

# 8. While Loop: Countdown (10 to 1)
count = 10
while count > 0:
    print(count)
    count -= 1
print("Countdown finished!")

# 9. While Loop: Sum of Even Numbers (1 to 20)
total = 0
num = 1

while num <= 20:
    if num % 2 == 0:
        total += num
    num += 1    
print("Sum of even numbers from 1 to 20:", total)

# 10. For Loop: Print Characters of a String
word = "Python"
for char in word:
    print(char)

# 11. Nested Loop: Multiplication Tables (1 to 3)
for i in range(1, 4):
    print(f"Multiplication Table for {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()  # Print a blank line after each table

for i in range(1, 4):
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print()  # separación

# 12. Break Statement (stop at 7)
for i in range(1, 11):
    if i == 7:
        break
    print(i)

# 13. Continue Statement (skip 5)
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# 14. If-Statement with Logical Operators
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("Day off")
else:
    print("Workday")

# 15. Prime Number Check
num = 11
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime")
else:
    print("Not Prime")

 """ 


""" 
# 1. BREAK STATEMENT

for i in range(1, 11):
    if i == 7:
        break
    print(i)

# 2. CONTINUE STATEMENT
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)


# 3. NESTED LOOPS (Loops dentro de loops)

for i in range(3):
    for j in range(3):
        print(f"i: {i}, j: {j}")

"""


# 1. Create a List
fruits = ["apple", "banana", "cherry"]
print(fruits)


