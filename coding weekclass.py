#Coding Week problems
#1 - Write a loop to print the first 25 perfect squares.

for i in range(25): #review list
    print((i+1)**2)
    
#2- Write a loop to count the number of 'a' characters in a string. Do not use any special 
#string methods, just indexing. (LOC: 6 – including printing the result))

my_str = str(input("Enter a word and I'll tell you how many 'a''s are in it: "))
count = 0
for c in my_str:
    if c == 'a':
        count+=1
print (count)

'''
#3 Write a loop to print all the perfect squares less than or equal to a number input by the
user. You should not print any perfect squares greater than the number the user inputs.
Test your code with the input 1000 and 0 (as well as other test cases). (LOC: 8)
'''

n = int(input("Enter a number: "))

for i in range(1,n):
    if (i**2) <= n:
        print(i**2)

'''
4 - Using the random module and the random.randint() function (use help to get the details)
and a loop, generate a list of 100 random integers between 10 and 500 inclusive. (LOC: 5)
'''

import random

list = [ ] #review random
for i in range(100):
    list.append(random.randint(10, 500))

print(list)

'''
Write a function that takes the list resulting from Q4 and outputs the minimum value
in list, the maximum value in the list, the sum of the values in the list, and the average of
the values in the list. Do not use the min(), max(), and sum() functions. You should do this
only using loops, indexing, and if-statements. (Hint: you should only use one loop in your
function). (LOC: 19 – including the code for Q4 and not including comments and
docstring
'''

import random

def min_max_sum_avg(my_list):
    
list = [ ] #review random
for i in range(100):
    list.append(random.randint(10, 500))

print(list)

my_sum = 0
my_min = 0
my_max = 0

for num inm my_list:
    my_num += num

    if num< my_list:
        my sum + = num
    
    if num< my_min:
        my_min = num
    elif num > my_max:
        my_max = num
    
    print("min", my_min)
    print("max", my_max)
    print("sum", my_sum)
    print("avg", my_sum/len(my_list))
    
        




