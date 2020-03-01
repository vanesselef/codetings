#tuples - immutable lists
nums = ([1,2,3])
print(nums, type(nums))
nums = ([1,2,3],)
print(nums, type(nums))

life =[('Canada', 76.5), ('United States', 75.5), ('Mexico', 72.0)]
print(life)
life[0] = life[1]
print(life)

#assign multiple variables at once
(x,y) = (4.2,3.1)
my_tuple = (x,y)
print(my_tuple)

x = 7
y = 3
tmp = y
y = x
x = tmp
print(x,y)

x = 7
y = 3
x,y = y,x
print(x,y)

#packing and unpacking
b = ("Bob", 19, "ME")
print(b)
name, age, program = b
print(name)
print(age)
print(program)
name, age, program = "Bob", 19, "ME"
print(name)
print(age)
print(program)

#sets
#{ brackets

vowels = {'a', 'e', 'i', 'o', 'u'}
print(vowels, type(vowels))
l = list(vowels)
print(l)

s = set([1,2,3,4,5,5])
print(s)
l = list(s)

vowels = {'a', 'e', 'i', 'o', 'u','a', 'e', 'i', 'o', 'u'} #ignores duplicates
print(vowels, type(vowels))
print(l)

#set operations

s = {1,2,3}
t = {3,4,5}
s |= t
print(s)



# intersection - prints elements common to both s&t
#no indexing - cant perform slicing
#holds distinct itmes - no duplicates

prime = {1, 2, 3, 5, 7, 11, 13, 17, 19, 23}
fib = {1, 1, 2, 3, 5, 8, 13, 21}
odd = set(range(1, 25, 2))
print(prime.intersection(fib))
print(prime & fib)

'''
s.issubset(t)	s <= t	test whether every element in s is in t
s.issuperset(t)	s >= t	test whether every element in t is in s
s.union(t)	s | t	new set with elements from both s and t
s.intersection(t)	s & t	new set with elements common to s and t
s.difference(t)	s - t	new set with elements in s but not in t
s.symmetric_difference(t)	s ^ t	new set with elements in either s or t but not both
s.copy()	N/A	new set with a copy of s
'''
#symmetric difference
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }
C = {}

print(A.symmetric_difference(B))
print(B.symmetric_difference(A))

print(A.symmetric_difference(C))
print(B.symmetric_difference(C))

A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }

print(A ^ B)
print(B ^ A)

print(A ^ A)
print(B ^ B)


#issubset
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y) 

print(z)

#true 

#issuperset
w = x.issuperset(y) 
print(w)

#false

#dictionaries

student_grades = {"John" : 'A+', "Brad" : "C-"}
print(student_grades)

bird_observations = {'canada goose' : 1, 'northern fulmar': 3}
print(bird_observations)
print(bird_observations['canada goose'])

'''
my_dict[key]	Indexing operation – retrieves the value associated with key.	john_grade = my_dict['John']
my_dict[key] = value	Adds an entry if the entry does not exist, else modifies the existing entry.	my_dict['John'] = 'B+'
del my_dict[key]	Deletes the key:value from a dict.	del my_dict['John']
key in my_dict	Tests for existence of key in my_dict	if 'John' in my_dict
'''
my_dict = {} # dictionary
my_set = set() # create empty set

my_dict["john"] = ['B+', 'A']
print(my_dict)

#nested dictionary
nested = {"john" : {"APS106" : 80, "CME185" : 50}}
print(nested)

#dictionary methods
#clear
d = {"bob":2, "jane":3}
print(d)
d.clear()
print(d)
#{'bob': 2, 'jane': 3}
#{}

#gett
d = {"Bob":2, "Jane":3}
print(d)

print(d.get("Jane", "N/A"))
print(d.get("Chad", "N/A"))
#print(d.get("Chad"))

print(d["Jane"])
'''
{'Bob': 2, 'Jane': 3}
3
N/A
None
3
The following produces an error
'''
d = {"Bob":1, "Jane":42}
print(d)

val = d.pop("Bob")
print(d)
print("val =",val)

val2 = d.pop("John", "N/A")
print(d)
print("val2 =", val2)




key_list = ["bob", "jane"]
value_list = [1, 42]
new_d = {}

for i in range(len(key_list)):
    new_d[key_list[i]] = value_list[i]
    #new_d["bob"] = 1
print(new_d)
hand = ["jack", "king"]
deck = ["spades", "joker"]


value = 0
for i in hand:
    if i == "jack" or i == "king" or i == "queen":
        value == 10

print(value)



