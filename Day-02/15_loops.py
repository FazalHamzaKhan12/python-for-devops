# Loops repeat a block of code.
# Python has two main loops: for and while.

# for loop - repeats a fixed number of times, often over range().
print("For loop:")
for number in range(1, 6):
    print(number)

# while loop - repeats while a condition is True.
# We must update the counter to avoid an infinite loop.
print("While loop:")
count = 1

while count <= 5:
    print(count)
    count += 1  # increase count by 1 each time

# break - stops the loop immediately.
print("Break example:")
for number in range(10):
    if number == 5:
        break  # stop the loop when number reaches 5
    print(number)

# continue - skips only the current iteration.
print("Continue example:")
for number in range(5):
    if number == 2:
        continue  # skip 2 and move to the next number
    print(number)