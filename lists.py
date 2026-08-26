items = ["apple", "banana", "cherry", 100, True, 3.14, 3 + 2j]

# print(len(items))
# print(type(items))

first_index = 0  # -len(items)
last_index = len(items) - 1  # -1

#CRUD
#C - Create
#R - Read
#U - Update
#D - Delete

nums = [1, 2, 3, 4, 5]

#CREATE

# append(value) -> adds element at last index
# insert(index, value) -> adds element at any specified index

nums.append(10)
# print(nums)

nums.insert(2, "hello")
# print("inserted", nums)
nums.insert(10, "hii")

print("Added",nums)
# print(len(nums))

#READ
# print(nums[-len(nums)])

#UPDATE
nums[4] = "four"
print("updated", nums)
#DELETE

#del -> keyword
#pop(index = "-1") -> method
#remove(value) -> method

del nums[2]
print("deleted", nums)

nums.pop()
print("popped", nums)
nums.pop(3)
print("popped Index", nums)

nums.remove(10)
print("removed", nums)


n = [1,2,3,2,4,2,2]
n.remove(2)
print(n)