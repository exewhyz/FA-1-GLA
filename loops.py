# Loop Works on List,Tuple,String

# Type of loops
# 1. for loop
# 2. while loop

text = "Python Programming"
# print(text.upper())
# EVEN INDEX chars (P,t,o," ",r,g,a,m,n)

# for value in text:
#     print(value)


# nums= [1,2,3,4,5]
# for num in nums:
#     print(num)
    
    

"""
SYNTAX

for value_name in str/list/tuple_name:
    #logic
"""

# n = [54, 6, 9, 3, 2]

# for value in n:
#     if value % 2 == 0:
#         print(value,"is Even")
#     else:
#         print(value, "is odd")


# len()
# type()
# print()
# input()
# sum()
# max()
# min()
# abs()
# int()
# float()
# complex()
# str()
# sorted()


# range(start,stop,step) -> int

# print(range(6))
# print(list(range(6)))
# print(list(range(2,6)))
# print(type(range(6)))

# for i in range(11):
#     print(i)
    
# for value in range(1,101):
#     value % 2 == 0 and print(value)

# for value in range(2,101,2):
#     print(value)
    
# for ch in "hello":
    # print(ch)
    
# write a program to check if student got less than 50 marks in any of the subjects.
# marks = ()
# ispass = True

# for m in marks:
#     if m < 50:
#         ispass = False

# if ispass and len(marks) > 0:
#     print("Student is pass in all subjects")
# else:
#     print("Student is fail")

nums = [1,2,3,4,5,6]
# nums = map(float, input().split(" "))

# for number in nums:
#     if number > 50:
#         print("Greater than 50")
#     else:
#         print("Less than 50")



prices = [99, 199, 599, 999, 499, 699, 299]


# print(sum(prices))
# promo_code = 10
# total = 0

# for p in prices:
#     if p >= 200:
#         total = total + p - 0.1 * p
#     total = total + p

# print(total)




# # print(max(prices))

# maximum = prices[0]
# for p in prices:
#     if p > maximum:
#         maximum = p
        
# print(maximum)


# calculate the total after multiplying numbers starting from 1 to 100 (including 100)
# Factorial of 100?

# total = 1
# for n in range(1,6):
#     total = total * n

# print(total)

# c = [1,2,3,4,5]
# reversed_list = []
# for v in c:
#     reversed_list.insert(0,v)
# print(reversed_list)

# count of vowels in a string

# vowels = "aeiou"
# text = input("enter your text: ").strip().lower()
# count = 0
# for ch in text:
#     if ch in vowels:
#         count += 1
# print(count)


# count and print all prime numbers from 1 to 20


# check if a number is prime or not

# n = int(input("Enter a number: "))

# if n < 2:
#     print("Not prime")
# else:
#     isprime = True
#     for num in range(2,n):
#         if n % num == 0:
#             isprime = False
#     if isprime:
#         print("Prime")
#     else:    
#         print("Not Prime")


# break, continue and pass

# break -> stops the execution of loop


# for i in range(1, 10):
#     if i == 7:
#         break
#     print(i)
    
    
# for i in range(1,10):
#     print(i)
#     if i == 5:
#         continue
    

# for i in range(1,10):
#     if i == 5:
#         print("Before pass")
#         pass
#     print(i)