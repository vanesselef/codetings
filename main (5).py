'''
Feb 5, 2020
The list
general form: [element1, elemnt2, ...... elementN]
'''
grades = [80, 90, 70]

print (grades[0])
print(grades[1])
print(grades[2])

print(90 in grades)
print(60 in grades)

print(len(grades))

print(min(grades))

print(max(grades))

print(sum(grades))

big_grades = [80, 90, 60, 40, 99]
print(min(big_grades[1:4]))

subjects = ["bio", "cs", "math" , "history"]
print(len(subjects))
print(min(subjects))
print(max(subjects))
#print(sum(subjects)) = error

mixed_list = [1, "a", "no", 47.5]
print(len(mixed_list))
#print(min(mixed_list))
#print(max(mixed_list)
#print(sum(subjects)) = error

grades = [["Assignment 1", 80],["Assignment 2", 90], ["Assignment 3", 70]]

print(grades)

sublist = grades[0]
print(sublist)
(print(sublist[0]))
print(sublist[1])
print(grades[0][0])

#LISTS ARE MUTABLE!
classes = ["chem", "bio", "cs", "eng"]
print(classes)
classes[2] = "math"
print(classes)

classes[0] = 17
print(classes)

classes[1] = [1,2,3]
print(classes)

lst1 = [11, 12, 13, 14, 15, 15, 17]
print("lst1: " + str(lst1))

'''
lst2 = lst1
lst1[-1] = 18
print("lst1:" + str(lst1))
print("lst2:" + str(lst2))


lst_a = [1,2,3,4]
lst_b = lst_a
lst_c = list(1st_a)
print(lst_a)

'''
colours = ["yellow" , "blue"]
colours.append("red")
print(colours)

colours.extend(["pink", "green"])
print(colours)

bad_colours = colours[:]
bad_colours.append(["black", "white"])
print(bad_colours)

c = colours.pop()
print(colours)
print(c)

c = colours.pop(1)
print(colours)
print(c)

c = colours.remove("red")
print(colours)
print(c)




