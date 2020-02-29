#coding week problems

#EASY
#1 
for i in range(1, 26):
    print(i**2)
    
count = 0
word = input("please enter a word:")
for i in word:
    if i == 'a':
        count+=1
print(count)

#3
high = int(input("enter a number:"))
for i in range(1, high):
    if i**2 <= high:
        print(i**2)
        
#4
high = int(input("enter a number:"))
for i in range(1, high):
    if i**2 <= high:
        print(i**2)


#MEDIUM
#1

max = 9
for first in range(max-1):
    for second in range(first+1, max):
        for third in range(second+1, max+1):
            print(first, second, third)
            
def findprimes(num)
num = int(input("Enter a number"))]
lst = []
for i in range(1, num-1, 2)
    while 
