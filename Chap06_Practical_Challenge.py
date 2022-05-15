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

'''
Question 7
Write code to calculate Fibonacci numbers. Create list containing
first 20 Fibonacci numbers, (Fib  numbers made by sum of preceeding
two. Series starts 0 1 1 2 3 5 8 13 ....)
'''
fib_list = [0,1]
lenght = 20
for i in range(1,9999):
    if len(fib_list) <= lenght:
        fib_list.append(fib_list[i] + fib_list[i-1])
    else:
        break
    #print(len(fib_list))
print(fib_list)


'''
Question 8
The previous question was the first to contain comments. Go back
through the other questions in this file and add comments to the
solutions.
'''

'''
Question 9

     *****
     *
     ****
     *
     *
     *
Can you draw this using python? (comment the solution code)
'''

for i in range(1,7):
    for j in range(1,6):
        if i ==1 and j < 5:
            print("*", end=" ")
        elif i == 2 and j < 3:
            print("*")
        elif i==3 and j < 4:
            print('*', end=" ")
        elif i > 4 and j < 3:
            print("*") 

'''
Question 10
Write some code that will determine all odd and even numbers
between 1 and 100. Put the odds in a list named odd and the evens
in a list named even.
'''

odd = []
even = []

for i in range (1,101):
    if i % 2 == 0 :
        odd.append(i)
    else:
        even.append(i)
print(odd)
print(even)
