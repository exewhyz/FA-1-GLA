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

filter_unique_value([20,10,10,40])