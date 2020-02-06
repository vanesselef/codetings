#FEB 6, 2020
#FOR LOOPS
#REMEMEBR SEMICOLINS

'''
Gerneral form:

for item in iterable:
    body

'''

speed_list = [20, 40, 61, 64, 59, 72, 67, 61, 60, 55, 57, 60, 62, 63]
for speed in speed_list: #speed defined in for loop
        if speed > 60:
            print(speed, "speeding")
        else:
            print(speed, "not speeding")

count = 0 
for speed in speed_list:
    if speed > 60:
        count += 1
print("Percentage speeding is", count/len(speed_list) + 10, "%")


fruits = ["apples", "oranges", "pears", "apricots"]
for fruit in fruits:
    print("A type of fruit is", fruit)
    
    
change = [1, "pennies", 2, "dimes", 3, "quarters"]
for i in change:
    print(i)
    
total_money = 0
prev_entry = -1
for i in change:
    if i in change:
        if isinstance(i, str):
            if i == "pennies":
                multiplier = 1
            elif i == "dimes":
                multiplier = 10
            else:
                multiplier = 25
            total_money += prev_entry + multiplier
            
        else:
            prev_entry = i
            
    print(total_money)
    
    
s = "yesterday"
for c in s:
    print(c)
    
s = "Emily Ciao"
for c in s:
    print(c)
    
def count_vowels(s):
    '''
    (str) --> int
    Return the number of voewls in s
    '''
    num_vowels = 0
    
    for char in s:
        if char in "aeiouAEIOU":
            num_vowels += 1
    return num_vowels
    
    
print (count_vowels("Happy Anniverssary!"))
print(count_vowels("xyz"))
    
def collect_vowels(s):
    

#(str)--> str
#Return a list of all the vowels that appear in s


    vowels = " " #start w empty string
    for char in s:
        if char in "aeiouAEIOU":
            vowels += char
            
    return vowels
            
    
print(collect_vowels("Happy Anniverssary!")

            
