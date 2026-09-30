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