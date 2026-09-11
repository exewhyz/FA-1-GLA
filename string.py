a = "hello"
# a = "Hello"

# a[0] = "H"
# del a[0]
# print(a)

"""
Strings are immutable

READ - Possible
CREATE - Not possible in string => AttributeError
UPDATE - Not possible in string => TypeError
DELETE - Not possible in string => TypeError(del) or AttributeError(pop,remove,clear)
"""


b = "hello how are you"
print(len(b))
print(type(b))

# b = "Hello how are you"

# b = "K" + b[1:] # "K" + "ello how are you" = "Kello how are you"


string1 = "" or ' ' or """Hello""" or ''''''
# string = ' '
# print(len(string1))

c = "hello how are you"
# print(c[8:5:-1])

print("Hello" + " " *5 + "world")

print("#"* 20)

# Membership Opeartor ('in' and 'not in') -> bool

message = "hello world"

# print(" " in message)

# check if the string is like an email or not

#   test@gla.in

email = "test@gla.in"

# if "@" in email and "." in email:
#     print("Email is valid")
# else:
#     print("Email is not valid")
    
# check if the string is palindrome or not

input_string = input("Enter your string: ")

if input_string == input_string[::-1]:
    print("it is palindrome")
else:
    print("it is not palindrome")
    
    
    
"""
A shop records the following information:
item = "Laptop"
price = 45000
quantity = 2
discount = 10

Write Python statements to:
1. Calculate the total price before discount. 
2. Calculate the discount amount and final payable amount. 
3. Display the final amount along with its data type.
4. Modify the program so that the quantity is taken from the user instead of being fixed as 2.
"""