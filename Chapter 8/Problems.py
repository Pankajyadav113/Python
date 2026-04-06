# Problem 1

def greatest(a, b, c):
    if(a>b and a>c):
     return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c

a = int(input("Enter number a: "))        
b = int(input("Enter number b: "))        
c = int(input("Enter number c: "))
print(greatest(a, b, c))        


# Problem 2 

def f_to_C(f):
    return 5*(f-32)/9

f = float(input("Enter temperature in F: "))
print(f"{round(f_to_C(f), 2)} Degree C")     # round and 2 is use for to get output at 2 decimal places


# Problem 3
print("a")
print("b")
print("c", end="")
print("d", end="")


# Problem 4

def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n

print(sum(4))        


# Problem 5

def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)

pattern(3)        


# Problem 6

def inch_to_cms(inch):
    return inch * 2.54

n = int(input("Enter value in inches: "))
print(f"The corresponding value in cms is {inch_to_cms(n)}")    


# Problem 7

def rem(l, word):
    n = []
    for item in l:
        l.remove(word)
        return l
        

l = ["Harry", "Rohan", "Shubham", "an"]
print(rem(l, "an"))



def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["Harry", "Rohan", "Shubham", "an"]
print(rem(l, "an"))



# Problem 8

def multiply(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n * i}")

multiply(5)        












def greatestnumber(a, b, c):
    if(a>b and a> c):
        print(f"{a} is the greatest number")
        return a
    elif(b>a and b>c):
        print(f"{b} is the greatest number") 
        return b   
    else:
        print(f"{c} is the greatest number") 
        return c
a = int(input("Enter the first number: "))
b = int(input("Enter the first number: "))
c = int(input("Enter the first number: "))        
print(greatestnumber(a, b, c))           


def f_to_c(f):
    return 5*(f-32)/9

f  = float(input("Enter temperature in F: "))
print(f"{round(f_to_c(f), 2)}°C")


print("a")
print("b")
print("c", end="")
print("d", end="")



def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n
print(sum(4))        


def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)
pattern(3)


def inch_to_cms(inch):
    return inch * 2.54
inch = int(input("Enter value of inches: "))
print(f"The corresponding value in cms is {round(inch_to_cms(inch), 2)} cms")


def rem(l, word):
    n = []
    for item  in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
l = ["Harry", "Rohan", "Shubham", "an"]
print(rem(l, "an"))



def multiply_table(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")

multiply_table(5)