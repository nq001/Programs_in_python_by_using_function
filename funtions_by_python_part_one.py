# Write a Python function to find the maximum of three numbers.

def maximum (num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return f" the maximum number is {num1}  "
    elif num2 > num1 and num2 > num3:
        return f" the maximum number is {num2}  "
    else:
        return f" the maximum number is {num3}  "
print(maximum(10, 11, 5))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.

# Write a Python function to sum all the numbers in a list.Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

def sum_numbers_in_list (name_list):
    sum_of_list = 0 
    add = 0 # counter for index 
    for i in name_list:
        s = name_list[add] # s to keep value of index [0]
        sum_of_list += s
        add += 1
    return f"the sum of this numbers in list is {sum_of_list} "   
number_of_list = [8, 2, 3, 0, 7]
print(sum_numbers_in_list(number_of_list))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Write a Python function to multiply all the numbers in a list.Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

def multiply_numbers_in_list (name_list1):
    total_numbers = 1
    
    for j in name_list1:
        total_numbers *= j
    return f" the multiply of numbers in this list is {total_numbers} "
listN = [8, 2, 3, -1, 7]
print(multiply_numbers_in_list(listN))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Write a Python function to calculate the factorial of a number (a non-negative integer). 
# The function accepts the number as an argument.

def calculate_factorial (facty_number):
    
    if facty_number == 0:
        return 1
    else:
        return facty_number * calculate_factorial(facty_number - 1)
num = int(input("Enter a number to compute the factiorial: "))
print(calculate_factorial(num))



# Naif Muhammed Saleh Abdullah Alqubalee