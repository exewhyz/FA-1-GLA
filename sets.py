numebrs = [1,2,3,4,5,6,1,4,7,2]

# print(list(set(numebrs)))


nums = {1, 2, 3, 4, 5, 6, 7,1,2}
# print(len(nums))
# print(type(nums))
# print(nums)

# CRUD O/P

#READ
# for value in nums:
#     print(value)

#CREATE - (add , update)
set_x = {1,2,3}
# set_x = {"a","z","b", "p"}
# set_x.add(4)
# set_x.update([5,6])
# set_x.update((5,6))
# set_x.update({5,6})
# set_x.update("56")

#REMOVE ()
"""
set_name.remove()
set_name.discard()
set_name.pop()
set_name.clear()
"""
# set_x.remove(100) #keyerror
set_x.discard(100) # no error
# print("removed element:",set_x.pop())
# set_x.clear()
# print(set_x)

# SET OPERATION

"""
1. Union
2. Intersection
3. Difference
4. isSubset
5. isSuperset
6. isDisjoint
"""

# Union
set_A = {1,2,3,4,5}
set_B = {2,3}
set_C = {10}

# print(set_A | set_B | set_C)
# print(set_A.union(set_B).union(set_C))

# print(set_A & set_B | set_C)
# print(set_A.intersection(set_B).union(set_C))

# print(set_A - set_B)
# print(set_A.difference(set_B))

# print(set_A ^ set_B)
# print(set_A.symmetric_difference(set_B)) #union - intersection

print(set_A >= set_B) # superset
print(set_A.issuperset(set_B))
print(set_B <= set_A) # subset
print(set_B.issubset(set_A))

print(len(set_A & set_B) == 0)
print(set_A.isdisjoint(set_B))