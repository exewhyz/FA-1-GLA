# collection of multiple data of different data type stored as an key : value pairs

# dictionary is unordered
# dictionary is mutable
# keys are unique
# keys are immutable
# keys are case sensitive
# values can be of any data type
# values can be mutable
# values can be same

# book = {}

# st_data = ["Aniket", 10, "test@test.com"] # 0,1,2
# st_data = ["Aditya", "test1@test.com", 20] # 0,1,2

# st_data = {
#     "name" : "Aniket",
#     10 :  "Ten",
#     3.14 : "Pi",
#     (1,2,3) : "Tuple",
#     True : "Success",
#     "age" : 10,
#     "email" : "test@test.com" 
# }



book = {
    "title" : "Python",
    "author" : "Aniket",
    "year" : 2022
}
# print(book["title"])

# book["publisher"] = "XYZ"
# print(book)
# book["author"] = "Rossum"

# del book["year"]

# p = {
#     "title" : "Speaker",
#     "price" : 2999,
#     "category" : "electronics"
# }
# p["price"] = p["price"] + p["price"] * 0.3
# print(p)


# Read methods

# get(key,default = None) -> Any | None

# print(book["title"])
# print(book.get("titlee", "Java"))

print(book.pop("year"))
print(book.popitem()) # => tuple[key,value] => (key, value)

# book.clear()
# z = book.copy()
print(list(book.keys())) # => dict_keys([keys]) => [keys]
print(list(book.values())) # => dict_keys([values]) => [values]
print(list(book.items())) # => dict_keys([(key,value)]) => [(key,value)]


"""
A college wants to maintain basic information about its students. Write a Python program to create a dictionary where the student's roll number is the key and the student's name is the value. 
1. Create an empty dictionary.
2. Take the roll number and name of multiple students from the user and store them in the dictionary. 
3. Display the complete student dictionary.
4. For the following input, write the expected output: 
Roll Number: 101, Name: Rahul 
Roll Number: 102, Name: Aman

"""


students = {}
number_of_students = int(input("Enter number of students: "))
for st in range(number_of_students):
    roll_number = input("Enter roll number: ")
    st_name = input("Enter name: ")
    students[roll_number] = st_name

print(students)

for key, value in students.items():
    print(f"Roll Number: {key}, Name: {value}" )