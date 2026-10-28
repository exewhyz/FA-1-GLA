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

with open("test.txt") as f:
    print(f.read())