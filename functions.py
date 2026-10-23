# function definition
# function call

# def function_name():
    # statements
    
# def add_two_numbers():
#     print(2+4)
    
# # function_name()
# add_two_numbers()
# add_two_numbers()

# parameter - data accept (define)
# argument - value pass to parameter (call)

def sum_three_nums(a,b,c):
    print(a+b+c)

num1 = 2
num2 = 4
num3 = 6
# sum_three_nums(10,20,30)
# sum_three_nums(1,2,3)
# sum_three_nums(1,2,3)
# sum_three_nums(num1,num2,num3)

# required parameter
# default/optional parameter


# def mul_nums(a,b=1):
#     print(a*b)
# def mul_nums(a=5,b):  #not possible
#     print(a*b)
    
# mul_nums(2,5)
# mul_nums(2)
# mul_nums()
# mul_nums(5)


# return keyword

# def sum(a,b):
#     print(a)
#     return a+b

# exec1 = sum("h","i")
# exec2 = sum("b","y")
# # print(exec1 + exec2)
# print(sum(exec1,exec2))

# def sum(a,b):
#     print(a)
#     return {f"{a}+{b}" : a+b}

# print(sum(10,20))

# def check_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
    
# def print_nums(n):
#     for num in range(1, n + 1):
#         print(num)

# print_nums(20)

# def sum_nums(numbers:list,start=0):
#     sum = start
#     for num in numbers:
#         sum += num
#     return sum

# print(sum_nums(start=10,numbers=[20,30,40]))

def create_user(name,email,password):
    return {
        "name" : name,
        "email" : email,
        "password" : password
    }

def filter_unique_value(dup_list:list | tuple | str| set):
    return list(set(dup_list))

# filter_unique_value([20,10,10,40])


# # local and global scope

# x = 10 # global variable

# def check_x():
#     global x
#     x = 20 # local variable
#     print("in:",x)
# print("out:",x)
# check_x()

# *args and **kwargs

# def avg(a,b,c):
#     return (a+b+c)/3
def avg(*nums):
    print(type(nums))
    print(sum(nums)/len(nums))

# avg(1,2,3,4,5,6)
# avg(1)
# avg(2,3)
# avg(2,3,5)

# * - tuple
# ** - dict

def summary(event_name,*contri, **leader_details):
    print("Event Name:", event_name)
    print("Amount Collected:", sum(contri))
    print("Avg Amount Collected:", sum(contri)/len(contri))
    print("Number of person:", len(contri))
    
    print("Leader Deatils:")
    for key,value in list(leader_details.items()):
        print(f"{key} : {value}")
        
# summary("Class Bday",10,5,21,6,name="Aryan",email="aryan@gla.in")


# lambda function

def add_two(a,b):
    return a+b

# lambda parameters : statement
lambda a,b : a+b

def test(a):
    return float(a)


# sorted([4,2,1,6],key=lambda a : float(a))

data = [("Ayush", 10),("Mayank", 5),("Karan", 15)]

# def filter_number(details):
#     return details[1]

# print(sorted(data,key=filter_number))
# print(sorted(data,key=lambda d : d[1]))

# hof - function accepts function as an argument
# callback - function as an argument

def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

def multiply(a,b):
    return a*b

def perform_operation(a,b,op):
    print(op(a,b))
    
# perform_operation(10,20,plus)
# perform_operation(10,20,minus)
# perform_operation(10,20,multiply)

def greet():
    print("hello")
    
# x = greet()
# x()
# print(x)

# map(callback,iterable) -> map
# print(list(map( lambda c : c.upper() ,["abc", "def"])))

# nums = input("enter 3 values: ").split()
# new_nums = list(map(int, nums))
# new_nums = list(map(int, input("enter 3 values: ").split()))
# print(type(new_nums))
# print(new_nums)

# filter(callback,iterable) -> filter

# map_callback => operation
# filter_callback => filtering condition

data = [4,2,1,5,9,8]

# for n in data:
#     if n % 2 == 0:
#         print(n)
        
print(list(filter(lambda n : n % 2 == 0,data)))



# map, filter and reduce

# map(callback,iterable) -> map
# filter(callback,iterable) -> filter

# iterable - str,list,tuple,dict,set,range,frozenset

d = [4,2,1,5,9,8]

# for n in d:
#     d[d.index(n)] = n * 2

print("before",d)
d = list(map(lambda n : n*2, d))

# even = []
# for n in d:
#     if n%2 == 0:
#         even.append(n)

even = list(filter(lambda n : n>7, d))

print("after",d)
print(even)