# open("file_path", mode="r", encoding="utf-8")


# file = open("test.txt")
# data = file.read()
# file.close()
# print(data)

# f1 = open("new.txt","w")
# f1.write("I am open in write mode")
# f1.close()

# f1 = open("new.txt","w")
# f1.write("Writing again")
# f1.close()

# f1 = open("new.txt","a")
# d = f1.write("hello hii")
# f1.close()
# print(d)

# with open("test.txt") as f:
#     print(f.read())
    
"""
Modes
1. r -> read
2. w -> write
3. a -> append
4. x -> create
5. t -> text
6. b -> binary
7. rb -> read binary
8. wb -> write binary
9. ab -> append binary
10. r+ -> read and write
11. +w -> write and read
12. +a -> append and read
"""

# file.read(size=-1) -> str
# -1 means everything
# size is number of characters
# file.write("content") -> int

# with open("test.txt", "r") as file:
#     print(file.read(2))
#     print(file.read(2))

# no_of_std = int(input("Enter number of students to add: "))

# for i in range(no_of_std):
#     st_name = input(f"Enter {i + 1} student name: ")
#     st_marks = int(input(f"Enter {i + 1} student total marks: "))

#     with open("student_data.txt", "a") as fl:
#         fl.write(f"{st_name}: {st_marks}\n")

# seek(), tell(), truncate()

# seek(int) -> int => moves the pointer from start and returns new position
# tell() -> int => location of pointer
# truncate(pointer) -> int => deletes from that pointer

# if pointer value is present then deletes from that place
# else it will start deleting from current position (file.tell())

# with open("test.txt", "r+") as f:
    # print("before seek",f.tell())
    # print(f.read(4))
    # print(f.seek(3))
    # print("after seek",f.tell())
    # f.truncate(2)
    
# with open("student_data.txt") as file:
    # for line in file:
    #     print(line)
    # print(file.readline())
    # print(file.readline())
    # print(file.readlines())
    
# data = ["Maitri: 1", "Aniket: 99"]
# data = ["Maitri: 1\n", "Aniket: 99\n"]
    
# with open("student_data.txt", "a") as file:
#     for d in data:
#         file.write(d+"\n")
    # file.writelines(data)
    
    
fil = open("student_data.txt")
print(fil.readlines())
print("before closing:",fil.closed)
fil.close()
print("after closing:",fil.closed)