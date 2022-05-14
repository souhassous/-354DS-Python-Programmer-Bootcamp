'''
Question 1
Ask the user for two numbers between 1 and 100. Then count from the
lower number to the higher number. Print the results to the screen.
'''
num_1 = int(input("Give me the first number :>>>>> "))
num_2 = int(input("Gibe me the seconde one  :>>>>> "))

print(num_1)
print(num_2)

first = min(num_1, num_2)
last = max(num_1, num_2)

print(first)
print(last)

for num in range(first, last + 1):
    print(num, end=" ")
    
'''
Question 2
Ask the user to input a string and then print it out to the screen in
reverse order (use a for loop).
'''
string = input("Give me a string to print out in the reverse order : >>>>> ")
print("string =",string)

lenght = len(string)
print ("lenght =",lenght)

print("the string in the reverse order ")
for i in range(1, lenght + 1):
    print(string[-i], end=" ")

'''
Question 3
Ask the user for a number between 1 and 12 and then display a times
table for that number.
'''

number = int(input("Give me a number between 1 and 12: >>>> "))
if number <= 12 and number >= 1:
    for i in range(1, 11):
        print (number , "x", i, "=", number * i)
        
else:
    print('Not the right number ')

"""
Question 4
Can you amend the solution to question 3 so that it just prints out all
times tables between 1 and 12? (no  need to ask user for input)
"""

for i in range(1,13):
    for j in range (1,13):
        print(i, "x", j , "=", i*j)

"""
Question 5
Ask the user to input a sequence of numbers. Then calculate the mean
and print the result
"""

num_sum =0
for i in range (1,6):
    print("The", i, "of", 5)
    num = int(input("Give me a number: >>>>> "))
    num_sum += num
print("The result")
print("Sum", num_sum)
print("Mean", num_sum / 5)

'''
Question 6
Write code that will calculate 15 factorial. (factorial is product of
positive ints up to a given number. e.g 5 factorial is 5x4x3x2x1)
'''
num = int(input("Give me a number to calculate his factorial : "))
print ("The factorail of the given number is:")
factorial = 1
while num > 0:
    factorial = factorial * num
    num -= 1
print(factorial)