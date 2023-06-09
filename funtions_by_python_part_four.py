# Write a program that takes in a list of integers and returns 
# a list of all unique pairs of integers in the list that add up to a given target value. For example, 
# given the list [1, 2, 3, 4, 5] and a target value of 7,
# the program should output the pairs (2, 5) and (3, 4).

def find_target (nums ,target):
    pairs = []
    for i in range(len(nums)):
        for k in range(i+1,len(nums)):
            if nums[i] + nums[k] == target:
                pairs.append((nums[i], nums[k]))
    return list(set(pairs))
nums = []
item = int(input("enter how many do you want items in list: "))
for n in range(item):
    it = int(input("enter a number: "))
    nums.append(it)
target = int(input("enter the target: "))

print(find_target(nums, target))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Write a program that takes in a list of integers and returns the length of 
# the longest increasing subsequence in the list. For example, 
# given the list [1, 3, 2, 4, 6, 5, 8], the program should output 4 
# (which corresponds to the subsequence [1, 2, 3 ,4 , 5, 6, 8]).

def find_longest_increasing_subsequence (nums):
    li = []
    a = 0
    for item in nums:
        mul = nums[a] * nums[a]
        if mul == item or mul < len(nums):
            li.append(item)
    return list(set(li))
lis = [1, 3, 2, 4, 10 ,12 ,11, 5, 8, 6]
print(find_longest_increasing_subsequence(lis))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Write a program that takes in a list of integers and returns 
# a list of all unique triplets of integers in the list that add up to a given target value. 
# For example, given the list [1, 2, 3, 4, 5] and a target value of 10, 
# the program should output the triplets (2, 3, 5).

def find_target_of_three_num (lis, target):
    pairs = []
    a = 0 
    for item in lis: #[1, 2, 3, 4, 5]
        for it in range(item + 1,len(lis)):
            for i in range(it + 1, len(lis)):
                if lis[item] + lis[it] + lis[i] == target:
                    pairs.append((lis[item], lis[it], lis[i]))
    return list(set(pairs))
lis = [1, 2, 3, 4, 5]
target = 10
print(find_target_of_three_num(lis, target))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Create a function that takes a list of numbers and returns only the even numbers in the list.

def cheack_nums (nums):
    even_list = []
    for item in nums:
        if item %2 == 0:
            even_list.append(item)
    return f"this is even number: {list(set(even_list))}"
lis = [1,7,8,5,4,2,36,7,4,1,2,3,8,7,5,6,1]
print(cheack_nums(lis))


# Naif Muhammed Saleh Abdullah Alqubalee