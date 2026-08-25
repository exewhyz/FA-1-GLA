# if 1 >2:
#     print("1 is greater than 2")
# else:
#     print("2 is greater than 1")
"""    
if cond:
    #logic
else:
    # logic
"""

# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You can vote")
# else:
#     print("You can't vote")
    
#else if ladder

# if age < 18:
#     print("You are minor")
# elif age >= 18 and age < 21:
#     print("You can drive")
# elif age >=21 and age < 60:
#     print("You are an adult")
# else:
#     print("enter valid age value")


# match/switch case

# b = True
# match b:
#     case False:
#         print("False case")
#     case True:
#         print("True case")
#     case _:
#         print("provide valid data")
    
print("""      
1. Create user data
2. Show all users data
3. Update user data
4. Delete user data
5. Exit
""")
choice = int(input("Enter the value for operation: "))
match choice:
    case 1:
        print("Create user data")
    case 2:
        print("Show all users data")
    case 3:
        print("Update user data")
    case 4:
        print("Delete user data")
    case 5:
        print("Exit")
    case _:
        print("Provide valid choice")