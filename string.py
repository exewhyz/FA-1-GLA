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
# print(len(b))
# print(type(b))

# b = "Hello how are you"

# b = "K" + b[1:] # "K" + "ello how are you" = "Kello how are you"


string1 = "" or ' ' or """Hello""" or ''''''
# string = ' '
# print(len(string1))

c = "hello how are you"
# print(c[8:5:-1])

# print("Hello" + " " *5 + "world")

# print("#"* 20)

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

# input_string = input("Enter your string: ")

# if input_string == input_string[::-1]:
#     print("it is palindrome")
# else:
#     print("it is not palindrome")
    
    
    
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

"""
String Methods

str_name.method_name()

1. lower()
2. upper()
3. capitalize()
4. title()
5. swapcase()
6. startswith()
7. endswith()
8. strip()
9. lstrip()
10. rstrip()
11. isdigit()
12. isalpha()
13. isalnum()
14. isspace()
15. split()
16. join()
17. index()
18. count()
19. find()
20. replace()
21. islower()
22. isupper()
23. istitle()
24. iscapitalize()
"""

# lower() => converts uppercase to lowercase
# upper() => converts lowercase to uppercase
# capitalize() => index = 0 char to upper and rest in lower
# title() => every word first letter in upper and rest will be in lower
# swapcase() => upper to lower and vice versa

text = "hELlO hOw arE You?"
print("OG:",text)
print("LOWER:",text.lower())
print("UPPER:",text.upper())
print("CAPITALIZE:", text.capitalize())
print("TITLE:", text.title())
print("SWAPCASE:", text.swapcase())

# startswith(value) -> bool => true if string starts with given value

# endswith(value) -> bool => true if string ends with given value

text2 = "python programming"
# print(text2.startswith("python prog"))
# print(text2.endswith("programming"))
#yth
# print(text2.startswith("y", 1,4))
# print(text2.endswith("h", 1,4))

# isalpha() -> bool => True if str has only alphabets
# isdigit() -> bool => True if str has only numbers
# isalnum() -> bool => True if str has both numbers and alphabets
# isspace() -> bool => True if str has only spaces

print("hello".isalpha())
print("15462".isdigit())
print("hello1y65".isalnum())
print("    ".isspace())