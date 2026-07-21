#arithematic oprations
a = 15
b = 4

print("Addition:", a + b)  

print("Subtraction:", a - b) 

print("Multiplication:", a * b)  

print("Division:", a / b) 

print("Floor Division:", a // b)  

print("Modulus:", a % b) 

print("Exponentiation:", a ** b)

#Comparison Operators

a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

#Logical Operators : Logical not, logical and, logical or

a = True
b = False
print(a and b)
print(a or b)
print(not a)

#Bitwise Operators
'''Bitwise NOT
Bitwise Shift
Bitwise AND
Bitwise XOR
Bitwise OR '''

a = 10
b = 4

print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)

#Assignment Operators

a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)


#Identity Operators

'''is          True if the operands are identical 
is not         True if the operands are not identical '''

a = 10
b = 20
c = a

print(a is not b)
print(a is c)

#Membership Operators

'''in            True if value is found in the sequence
not in           True if value is not found in the sequence'''

x = 24
y = 20
my_list = [10, 20, 30, 40, 50]

if (x not in my_list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in my_list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")


#Ternary Operator

'''[on_true] if [expression] else [on_false] '''

a, b = 10, 20
min = a if a < b else b

print(min)

'''Precedence and Associativity'''
