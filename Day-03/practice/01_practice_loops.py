# print all odd numbers from 1 to 20

# for i in range(20):
#     if(i % 2 == 1):
#         print(f"this is odd numbers{i}")


# print the table of 57

# for i in range(1, 11):
#     print(f" 57 * {i} = {57 * i}")


# print all multiples 3 from 1 to 50 but skip 15

# for i in range(1, 51):
#     if (i == 15):
#         continue
#     if(i % 3 == 0):
#         print(f"this is multiples of 3 {i}")


# take two integers a and b if input
# find and print the first number between 1 and 1000 that is divisibvle by both a and b

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

for i in range(1, 1001):
    if i % a == 0 and i % b == 0:
        print(f"{i} is divisible by {a} and {b}")
        break





