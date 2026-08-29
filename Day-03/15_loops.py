# # Loops repeat a block of code.
# # Python has two main loops: for and while.

# # for loop - repeats a fixed number of times, often over range().
# print("For loop:")
# for number in range(1, 6):
#     print(number)

# # while loop - repeats while a condition is True.
# # We must update the counter to avoid an infinite loop.
# print("While loop:")
# count = 1

# while count <= 5:
#     print(count)
#     count += 1  # increase count by 1 each time

# # break - stops the loop immediately.
# print("Break example:")
# for number in range(10):
#     if number == 5:
#         break  # stop the loop when number reaches 5
#     print(number)

# # continue - skips only the current iteration.
# print("Continue example:")
# for number in range(5):
#     if number == 2:
#         continue  # skip 2 and move to the next number
#     print(number)


# its a triangle pattern using while loop

# i = 5
# while i >= 0:
#     print(i * "*")
#     i -= 1

# i = 1
# while i <= 5:
#     print(i * "*")
#     i += 1


# for loops 

# 5 to 11

# for nums in range(5, 11):
#     print(nums)

# for nums in range(2 ,10, 2):
#     print(nums)


# for i in range(0, 6):
#     if i % 2 == 0: 
#         print(i, "is even")


# name = "Python"

# for character in name:
#     print(character)


# multiples of 3 [1 to 50] => 21 

for i in range(1, 51):
    if(i == 21):
        print("Found 21")
        continue
    if i % 3 == 0:
        print(i, "is multiple of 3")