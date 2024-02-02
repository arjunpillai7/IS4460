#This is a comment

print('Hello World!')

print('Chewbacca') # this is an object of type string.
print(3.4) # this is a number. Technically a float.


a = 5
b = 6

print(a+b)

A = 11
a = 77
print(a)
print(A)


print(type(A))

print(type(4.0))

def add_numbers(a,b):
  output = a + b
  return output
print(add_numbers(4,14)) # positional arguments.
print(add_numbers(b=10,a=7)) # named arguments.

name = "Tim"

def say_hello():
  name = "Arjun"
  return f"hello {name}"

print(say_hello())

