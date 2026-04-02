# friends = ["Apple", "Orange", 5, 345.06, False, "Akash", "Rohan"]
# print(friends[0])

# friends[0] = "Garapes"   # list are mutable
# print(friends[0])  

# print(friends[1:5])   # indexing also valid

# friends.append("Pankaj")  # append means at the end add
# print(friends)

friends.append("[122, 43]")
print(friends)

a = [12,23,34,35]
b = [24]
a.extend(b)
print(a)

# Using a tuple
a = [1, 2, 3]
b = (4, 5)
a.extend(b)
print(a) 

# Using a set
a = [1, 2, 3]
b = {4, 5}
a.extend(b)
print(a)  

# Using a string
a = ['a', 'b']
b = "cd"
a.extend(b)
print(a)  

# l1 = [1, 34, 62, 2, 6, 11]
# l1.sort()               # arrange in increasing order
# print(l1)

# l1.reverse()            # reverse the list
# print(l1)

# l1.insert(3, 3333)      # inserting in list at any index 
# print(l1)

# l1.pop(4)               # delete any particularr index number from list
# print(l1)

# l1.remove(2)              # delete that particular value from the list
# print(l1)

# value = l1.pop(3)
# print(value)
# print(l1)