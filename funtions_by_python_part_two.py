# Write a Python function to check whether a number falls within a given range.

def check_number (num):
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    if num in range(n1,n2):
        return f" {num} this number is inside the range "
    else:
        return f" {num} this number is outside of the range"
numb = int(input("Enter the number to check if number is find in the range: "))
print(check_number(numb))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Write a Python function that accepts a string and counts 
# the number of upper and lower case letters.

def find_up_low (text):
    low = 0
    upp = 0
    for char in text:
        if char.isupper():
            upp += 1
        else:
            if char.islower():
                low += 1
    return low , upp
te = input("enter the string: ")
sav = find_up_low(te)
print(f"{sav}\n")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# program to find largest number in list by using python function by using input

def find_max_number(numbers):
    largest = numbers[0]  # Assume the first number is the largest
    for number in numbers:
        if number > largest:
            largest = number
    return largest
# Example usage
my_numbers = []
num1 = int(input("enter how many numbers do you want add to list: "))
for i in range(num1):
    item = int(input("enter a number: "))
    my_numbers.append(item)
largest_number = find_max_number(my_numbers)
print("The largest number is:", largest_number)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

lis1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Result = []
for item in lis1:
    if item %2 == 0:
        Result.append(item)
print(Result)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Naif Muhammed Saleh Abdullah Alqubalee