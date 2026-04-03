# Problem 1
# # 1. Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!



# words = {
#     "madad":"Help",
#     "kursi":"Chair",
#     "billi":"Cat"
# }
# word = input("Enter the word you want meaning of:")
# print(words[word])

# Problem 2
# 2. Write a program to input eight numbers from the user and display all the unique
# numbers (once).


# s = set()
# n = input("Enter number: ")
# s.add(int(n))
# n = input("Enter number: ")
# s.add(int(n))
# n = input("Enter number: ")
# s.add(int(n))
# n = input("Enter number: ")
# s.add(int(n))
# n = input("Enter number: ")
# s.add(int(n))
# n = input("Enter number: ")
# s.add(int(n))
# n = input("Enter number: ")
# s.add(int(n))
# n = input("Enter number: ")
# s.add(int(n))

# print(s)

# Problem 3
# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?


# s = set()
# s.add(18)
# s.add("18")
# print(s)

# problem 4

# s = set()
# s.add(20)
# s.add(20.0)      # same as 20  so python show the value of this set is 2 
# s.add('20')
# print(len(s))

# problem 5

# s = {}          # this is dictionary not a set

# problem 6 

# s = {}

# name = input("Enter friends name: ")
# lang = input("Enter language name: ")
# s.update({name: lang})

# name = input("Enter friends name: ")
# lang = input("Enter language name: ")
# s.update({name: lang})

# name = input("Enter friends name: ")
# lang = input("Enter language name: ")
# s.update({name: lang})

# name = input("Enter friends name: ")
# lang = input("Enter language name: ")
# s.update({name: lang})

# print(s)

# problem 7


# s = {}

# name = input("Enter friends name: ")
# lang = input("Enter language name: ")
# s.update({name: lang})

# name = input("Enter friends name: ")
# lang = input("Enter language name: ")
# s.update({name: lang})

# name = input("Enter friends name: ")
# lang = input("Enter language name: ")
# s.update({name: lang})

# name = input("Enter friends name: ")
# lang = input("Enter language name: ")
# s.update({name: lang})

# print(s)

# Problem 8

# in case of two persons have same name then in the output we got only one lang which was written in last


# problem 8

# s = {}

# name = input("Enter friends name: ")
# lang = input("Enter language name: ")
# s.update({name: lang})

# name = input("Enter friends name: ")
# lang = input("Enter language name: ")
# s.update({name: lang})

# name = input("Enter friends name: ")
# lang = input("Enter language name: ")
# s.update({name: lang})

# name = input("Enter friends name: ")
# lang = input("Enter language name: ")
# s.update({name: lang})

# print(s)

# in case of two persons have name fav lang then the output is normally printed as we put the input


# problem 9

# Can you change the values inside a list which is contained in set s?
# s  = {8,7,12,"Harry", [1,2]}