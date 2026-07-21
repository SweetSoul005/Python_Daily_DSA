'''Integers  Float  Complex'''
a = 5
b = 5.0
c = 2 + 4j

print(type(a)) # integer
print(type(b)) # float
print(type(c)) # complex


# Sequence Data Types
'''String  List  Tuple   '''
s = 'Welcome to the Geeks World'
print(s)
print(type(s))

# access string with index
print(s[1])
print(s[-1])


a = [1, 2, 3]
print(a)

b = ["Geeks", "For", "Geeks", 4, 5]
print(b[3])
print(b[-3])

t1 = (1,)
print(type(t1))

t2 = ('Geeks', 'For', 'Geeks', 1, 2)
print(t2[3])
print(t2[-3])

# boolean data type : Truthy and Falsy Values

print(type(True))
print(type(False))

if 1:
    print("1 is truthy")

if not 0:
    print("0 is falsy")



#Set Data Type : Sets are unordered and mutable collections used to store unique element


s1 = {"a", "a", "b", "c", "b"}
print(s1)

s2 = {"Geeks", "For", "Geeks"}
for i in s2:
    print(i)



#Dictionary Data Type

d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d[1])    
print(d.get(2))

