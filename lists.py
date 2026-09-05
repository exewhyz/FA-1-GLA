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

# print("Added",nums)
# print(len(nums))

#READ
# print(nums[-len(nums)])

#UPDATE
nums[4] = "four"
# print("updated", nums)
#DELETE

#del -> keyword
#pop(index = "-1") -> method
#remove(value) -> method

del nums[2]
# print("deleted", nums)

nums.pop()
# print("popped", nums)
nums.pop(3)
# print("popped Index", nums)

nums.remove(10)
# print("removed", nums)


n = [1,2,3,2,4,2,2]
# n.remove(2)
# print(n)

# count number of values present inside list
# list_name.count(value) -> int
count_of_value = n.count(3)
# print(count_of_value)

# index of first matched value of a list
# list_name.index(value,start=0,stop=len(list)) -> int 
m = [1,2,3,2,4,2,2,5]
# index_of_value = m.index(4,3,7)
# print("Index of value:",index_of_value)

# reverse a list
# list_name.reverse() -> None
x = [2,1,4]
# x.reverse()
# print("Reversed", x)

#sorting of list
# list_name.sort() -> None
# sorted(list_name) -> List
# x.sort(reverse=True)
# print("Sorted using sort:",x)
# sorted_using_sorted = sorted(x,reverse=True)
# print(sorted_using_sorted)



names = ["aniket", "jai","Jai", "ayush", "piyush", "aryan"]

# [6, 3, 3, 5, 6, 5]
# [3, 3, 5, 5, 6, 6]
# ["jai", "Jai", "ayush", "aryan", "aniket", "piyush"]
names.sort(key=str.lower)
# print(names)


t = ["a", "b", "Z", "B"]
# ["a", "b", "z", "b"]
# ["a", "b", "B", "Z"]
# t.sort(key=str.lower)
# print(t)

# k = [123, 456, 124, 457, 321]
# k.sort()
# print(k)

m = [1,2,3,4,-2,5,6,7,8,9,10]

def hello(num):
    return num % 2 == 0 and num + 1

m.sort(key=hello)
# [False, 2 +1 , False, 4 + 1, False, 6 + 1, False, 8 + 1, False, 10 + 1]
# [False, 3, False, 5, False, 7, False, 9, False, 11]
# [0 ,3,0,5,0,7,0,9,0,11]
# [0,0,0,0,0,3,5,7,9,11]
# [1,3,5,7,9,2,4,6,8,10]
# print(m)


# v = [12,10,True,"Aniket", -1 ,False,0]
# v.sort()
# print(v)


# p = [1,2,3]
# extend(iterable) -> None => adds multiple values at the end
# p.append([4,5,6])
# p.extend([4,5,6])
# print(p)

# Wrong property for str
# u = "hello"
# u.extend("world")
# print(u)

"""
Direct Built In Methods/Functions
1. max(iterable) -> depends on type of data in list
2. min(iterable) -> depends on type of data in list
3. sum 
"""

# print("Max of List",max([7,1,9,8,2]))
# print("Min of List",min([7,1,9,8,2]))
# print("Max of Str",max("hello"))
# print("Min of Str",min("hello"))
# print("Max of Tuple",max((1,2,3)))
# print("Min of Tuple",min((1,2,3)))


#Slicing => provides part of iterable(str,list,tuple)

# start:end:step

words = ["hello", "how", "are", "you", "?"]

# print(words[1:]) # without end value (end will be len(list))
# print(words[:3]) # without start value (start will be 0)
# print(words[:]) # without start and end values (start = 0 and end = len(list))

# print(words[::2])

numbers = [10,5,6,7,8,2,1,3,4,9]
numbers.sort(reverse=True) # [10,9,8,7,6,5,4,3,2,1]
numbers = numbers[::-1] # [1,2,3,4,5,6,7,8,9,10]
# options
# print(numbers[0::2])
# print(numbers[0:len(numbers):2])
# print(numbers[0:len(numbers):1])
# print(numbers[1::2]) # [2,4,6,8,10]


j = [1,2,3,4,5]

print(j[3:0:-2])