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