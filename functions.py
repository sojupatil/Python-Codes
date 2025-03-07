# 1. Simple addition of numbers from Py functions

def add(a,b):
    return a+b
print(add(251,15))

# 2. Addition of numbers by accepting values

def add_b(a,b):
    return a+b

first_b = int(input("Enter first number"))
second_b = int(input("Enter second number"))
print(add_b(first_b,second_b))

# 3. Accepting values and performing sum and product.

def num_c(a,b):
    return a+b , a*b

first_c = int(input("Enter first number"))
second_c = int(input("Enter second number"))

sum_val, prod_val = num_c(first_c, second_c)  

print(f"Addition are {sum_val} and multiplication are {prod_val}")

# 4. Check if numebr is even or odd using functions 

def num_d(number_c):
    if number_c % 2 == 0:
        return "Even" 
    else:
        return "Odd" 
    
first_d = int(input("Enter number to check if number is even or odd"))
print(num_d(first_d))

# 5. Factorial using recursion 

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

num_e = int(input("Enter number for factorial"))
fact(num_e) 