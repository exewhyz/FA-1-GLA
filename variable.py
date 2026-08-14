name = "Aniket"
age = 20
pi = 3.14
is_student = False

a_b_c = "abc"

type_of_pi = type(pi)
print(type_of_pi)


"""
Data Types
String - str
Integer - int
Float - float
Complex (Real + Imaginary) - complex
Boolean - bool
None - None
"""

#String
#double quote
city = "Noida"
#single quote
country = 'India'
#triple (double/single) quote
college = """GLA University"""
year = '''2026'''

#Numbers
#int
a = 10
#float
b = 5.4
#complex
c = 3 + 4j

#Boolean
x = True #1
y = False #0

#None
z = None

# print(isinstance(x,bool)) #Data, DataType -> Boolean(True/False)

number = "10"
new_number = int(number)
c_number = complex(new_number)
# print(c_number)
# print(isinstance(True, int))
# print(bool([1,2,3]))



num = 2 +(-7J)

print(type(num))
print(num.real)
print(num.imag)

print(int(num.real))
print(int(num.imag))

print(complex(5,8))
print(num.conjugate())
print(num.__abs__()) 


def count():
    print(15)
    
    
# count()

"""
1. python code
2. cpython
3. bytecode -> machine code
4. Python virtual machine
5. stop
"""
