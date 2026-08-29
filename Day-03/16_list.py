# list 
# a collection of items in a particular order

marks = [10, 20, 30, 40, 50, "3", 3.5, True, False]

# print(marks[0])  # prints the first element 


# print the lenth of the list

print(len(marks))  # prints the length of the list

# index values 
#  items in a list are indexed, the first item has index 0, the second item has index 1, and so on.

print(marks[3])  # prints the fourth element 

# in if we use - so its from opposite side -1 is the last element, -2 is the second last element, and so on.
print(marks[-1])  # prints the last element
print(marks[-2])  # prints the second last element

# slicing a list

# slicing a list - list {start: end}
# slicing a list is start , stop , step list[start:end:step]
print(marks[1:4])  # prints elements from index 1 to 3 
print(marks[:3])   # prints elements from the beginning to index 2
print(marks[2:5])  # prints elements from index 2 to 4
print(marks[1:5:2]) # prints elements from index 1 to 4 with a step of 2




for i in marks:
    print(i)  # prints each element in the list


# list are mutable - we can change the elements in a list
marks[0] = 100  # change the first element to 100

print(marks)  # prints the updated list

marks.append(60)  # add an element to the end of the list
print(marks)  # prints the list with the new element

marks.insert(1, 50)
print(marks )