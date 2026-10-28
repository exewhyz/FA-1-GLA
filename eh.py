# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     try:
#         print(num1 / num2)
#     except ZeroDivisionError:
#         print("Cannot divide by zero")
# except ValueError:
#     print("Provide digits only in input")

# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     result = num1 / num2
# except ValueError:
#     print("Provide digits only in input")
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# else:
#     print(result)

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

# try:
#     num = int(input("Enter a number: "))
# except ValueError as e:
#     print("Error:",e)
# else:
#     print("Your Number:",num)
    


# raise TypeError
# raise ValueError("I am generated error")
# raise Exception("I am generated error")

# try:
#     age = int(input("Enter your age: "))
#     if age < 0 or age > 115:
#         raise TypeError("Age must be in range of 0 to 115")
#     print(age)
# except TypeError as e:
#     print("Error:", e)
# except Exception as e:
#     print("Other Error:", e)


# def withdraw(balance, amount):
#     if amount > balance:
#         raise ValueError("Insufficient balance")
#     return balance - amount
# try:
#     remaining_bal = withdraw(10, 15)
#     print("Remaining Balance:",remaining_bal)
# except Exception as e:
#     print("Error:",e)


# class InsufficientBalanceError(Exception):
#     pass

# def withdraw(balance, amount):
#     if amount > balance:
#         raise InsufficientBalanceError("Insufficient balance")
#     return balance - amount

# withdraw(10,15)


class InsufficientBalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise InsufficientBalanceError("Insufficient balance")
    return balance - amount

try:
    balance = 5000
    amount = int(input("Enter withdrawal amount: "))
    balance = withdraw(balance, amount)
except ValueError as e:
    print("Invalid amount:", e)
except InsufficientBalanceError as e:
    print("Transaction failed:", e)
else:
    print("Withdrawal successful")
    print("Remaining balance:", balance)
finally:
    print("Thank you for using our banking system")