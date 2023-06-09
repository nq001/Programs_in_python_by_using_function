# write a python function to reserve items in this 
# list= [[1,2,3,4,5,6],[2,3,5,8,],[2,7,10,8]] and sum items in list[1] and list[2] 
# then print total of list[1] and list[2]
# and average of them the print list original but are reverses

def res_sum_avrg (numbers):
    
    # some variables
    sum_lists = 0
    average = 0
    rever_lists = []
    
    # reverses 
    for items in numbers:
        items.reverse()
        rever_lists.append(items)
    
    # sum
    add = 0
    add2 = 0
    for i in numbers:
        summ = numbers[1][add] + numbers[2][add2]
        sum_lists += summ
    
    # average
    aver = sum_lists / len(numbers[1] and numbers[2])
    average += aver
    
    return f"reverse: {rever_lists} \n sum of list[1] and list[2]: {sum_lists}\n average of them: {average}"
    
lists = [[1,2,3,4,5,6],[2,3,5,8,],[2,7,10,8]]
defi = res_sum_avrg(lists)
print(defi)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# program by using python function to show length in list without function len

def len_list(nums):
    count = 0
    for item in nums:
        count += 1
    return f"the length of this list is: {count} "
my_list = [1,2,3,4,5,6,7,8,9]
print(len_list(my_list))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# input Sample List : [1,2,3,3,3,3,4,5]
# output Unique List : [1, 2, 3, 4, 5]

def re_new_list(list1):
    
    lis = []
    for item in list1:
        if item not in lis:
            lis.append(item )
            
    return f"unique list : {lis}"

num_stop = int(input("Enter a number to know length list: "))
my_list = []
for k in range(num_stop):
    it = int(input("Enter a number: "))
    my_list.append(it)
    
print(re_new_list(my_list))
print("="*40)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# write a python program to reverse in list the first number rather tha last number by 1D list

list = [1,2,3,4,5,6] # Example list

# Swapping the first and last elements using slicing
list1[-1], list1[0] = list1[0], list1[-1]
print(list1) # Output: [6,2,3,4,5,1]


# Naif Muhammed Saleh Abduallah Alqubalee

