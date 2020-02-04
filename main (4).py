
#APS106 Midterm 1 review

#1 - ARHITMETIC OPERATORS AND PRECEDNECE
#addition
print(2 + 2)
#4

#subtraction
print(-2 - -1.3)
#-0.7

#multiplication
print(2*4)
#8

#power 
print(2**3)
#8

#division
print(4/-2.3)
#-1.7391304347826089

#floor division - rounds to closest whole number
print(4//-2.3)
#-2, 
#actually -1.7391304347826089, but rounds UP to closest whole #

print(4//2.3)
#1
#4/2.3 is 1.7391304347826089, but rounds DOWN to closest whole #

#modulus (think of this like remainder)
print(8%3) 
#2
print(9%3)
#0

'''
Precedence (highest to loweest)
** 
- (negation not subtraction)
*, /, //, % (evaluate left to right)
+, - (left to right)
'''

x = 2 + 5*2 **2
# 2 + 5*(4)
# 2 + 20
print(x)
#22

#2 - BUILTINS
#takes the absolute value
x = abs(-2)
print(x)
#2

x = True
print(bool(x))

print(chr(65))
#A

print(ord("A"))
#65

print(chr(97))
#a

print(ord("a"))
#97

print(float(23))

str1 = "geek"
print(id(str1))
#returns identity of an object

print(len("hello"))
#5
print(len("ciao"))
#4

key = 2.0
x = isinstance(key, float)
print(x)

print(round(23.238, 2))

#3 - ESCAPE SEQUENCES
#\n  = NEW LINE
print("Hi my \n name is Vanessa")

#\' = SINGLE QUOTES
print("Hi my name is \'Vanessa\'")

#\" = DOUBLE QUOTES
print("Hi my name is \"Vanessa\"")

#\\ - when u wanna print \n
print("Hi my name is \\n Vanessa")

import math

print(math.ceil(-1.2))
#-1

print(math.ceil(1.2))
#2

print(math.floor(1.2))
#1

print(math.floor(-1.2)) 

#FLOOR AND CEIL WOR COUNTERINTUITIVELY FOR HOW U THINK THEY WOULD FOR NEG VALUES
#-2

#(math.degrees) = converts an angle from radians to degrees

print(math.e)
#2.718281828459045 

print(math.sqrt(2))
#1.4142135623730951  

print(not True)
#False

print(not not True)
#True

#4 - RATIONAL COMPARASIN
print(2 != 3)
#True

print(True == False)
#False

print(2==3)
#False

num = 4
num += 1
print(num)

x = 4
x -= 1
print(x)

y = 4
y *= 2
print(y)


#5 -STRINGS

#concatication
print("Hello" + "z")
#Helloz
print("2" + "3")
#23

print("Ciao" * 4)
#CiaoCiaoCiaoCiao

a = "Hello, World!"
print(a[1])
#e

z = "I'm boutta go off on this midterm"
print(z[-1])
#m

b = "Hello, World!"
print(b[2:5])
#INCLUSIVE ON FIRST, EXCLUSIVE ON LAST

swag = "ur nan"
print(swag[3:6])

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

a = "baguette"
print(a.rfind("e"))
#7






