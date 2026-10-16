
# numbers = [1,2,3,4,5]
# new_numbers =[]
# for num in numbers:
#     new_numbers.append(num*2)

# print(new_numbers)

# [statement/expression for value in iterable]
# print([num*2  for num in numbers]) # list comprehension
# print({num*2  for num in numbers}) # set comprehension


# [ statement for value in iterable if condition]

# print([ n for n in range(1,10) if n % 2 == 0])

# [statement1 if cond else statement2 for value in iterable]

# print([n*2 if n % 2 == 0 else n*3 for n in range(1,10)])

# even = []
# odd = []
# [even.append(n) if n % 2 == 0 else odd.append(n) for n in range(1,10)]
# print(even)
# print(odd)

# print({ f"number-{value}" : value for value in range(1,10) }) # dict comp
# print({ value for value in range(1,10) }) # set comp


# [statement for v1 in iterable1 for v2 in iterable2]

# print([(v1,v2) for v1 in range(1,4) for v2 in range(2,5)])


ids = [1,2,3,4,5]
names = ["ayush", "ankit", "mayank", "topi", "gangster"]

# print(list(zip(ids, names)))

print({key : value for key,value in zip(ids,names)})

