# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     try:
#         print(num1 / num2)
#     except ZeroDivisionError:
#         print("Cannot divide by zero")
# except ValueError:
#     print("Provide digits only in input")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
except ValueError:
    print("Provide digits only in input")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(result)

# try:
#     print(1 + "2")
# except TypeError:
#     print("Cannot add string and integer")


# try:
#     print(1 + "2")
# except ValueError as e:
#     print("provide digits only:", e)
# except Exception as e:
#     print("Other type of error:", e)
# finally:
#     print("process completed")

try:
    num = int(input("Enter a number: "))
except ValueError as e:
    print("Error:",e)
else:
    print("Your Number:",num)