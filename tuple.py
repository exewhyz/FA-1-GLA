# [ 1,2,3 ]  #List

#Tuple
t = ( 1, 2, 3, "Hello", True,3, ( "devansh" ), ["one", "hii"] )

# print(t[2:6])
# t.extend(6,len(t)) #AttributeError
# t[3] = "Bye" #TypeError
# del t[3] #TypeError

# print(t.index(True,3,7))

# tuple packing
nums = 1,2,3
# nums = (1,2,3)
# print(type(nums))

# tuple/list unpacking
# a,b,c = [4, 5, 6]

# h=input("Enter 3 values: ").split(" ")

# j,k,l = h

# p[0]
# p[1]
# p[2]

# d = 4
# e = 5
# f = 6
d,e,f = 4, 5, 6
# d,e,f = (4, 5, 6) # first packing into tuple and then unpacking of values


g = "hello"

# print(tuple(g))

f = (5, 3,6)

# f.sort()
# print(sorted(f))



s = [1,2,3] #X0024
# t = s #X0024 => copy both address and value
t = s.copy() #X0025 => copy only value
t.append(4)
s.pop(1)
# print("S", s)
# print("T", t)


# sum(list/tuple, start=0) -> int

# u = (1,2,3)
# u = (1,2,"a")
# u = ("a","b","c")
# u = (True, False,54)
u = []
sum_of_numbers = sum(u,start=-50)
# print(sum_of_numbers)



# take multiple numbers from single input statement and sum all.

# numbers = input("Enter your numbers to add: ").split()
# [ "1", "2", "3" ]
# k = map(int, numbers)
# print(list(k))


# check the tuple is same from left and right side(palindrome)

# m = (2, 5, 2)
# m = tuple(input("enter values: ").split())
# if m == m[::-1]:
#     print("It is palindrome")
# else:
#     print("It is not palindrome")
    
# take input from user and verify otp using the following data
otp = ("2", "4", "9", "7")
## user_otp = tuple(input("enter the otp: ")) # without space
# user_otp = tuple(input("enter the otp: ").split()) # with space

# if otp == user_otp:
#     print("OTP verified")
# else:
#     print("OTP not verified")