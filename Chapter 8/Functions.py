# Function Definition

def avg():
    a= int(input("Enter number a: "))
    b = int(input("Enter number b: "))
    c = int(input("Enter number c: "))
    average = (a+b+c)/3
    print(average)
avg()               # Function call
print("Thank you")
avg() 
print("Thank you")   
avg()    
print("Thank you") 


# Quick Quiz

def goodDay():
    print("Good Day")
goodDay()    

# Function with Arguments

def goodDay(name, ending):
    print("Good Day," + name)
    print(ending)

goodDay("Harry", "Thank you")
goodDay("Ronaldo", "Thank you")
goodDay("Sohan", "Thanks")



def goodDay(name, ending):
    print("Good Day," + name)
    print(ending)
    return "ok"               # return value concept

a = goodDay("Harry", "Thank you")
print(a)




def goodDay(name, ending = "Thank you"):
    print("Good Day," + name)
    print(ending)

goodDay("Harry", "Thanks")
goodDay("Rohan")









def avg():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))

    average = (a + b + c)/3
    print(average)
avg()
print("Thank you!")    
avg()
print("Thank you!")    
avg()
print("Thank you!")    



def goodDay():
    print("Good Day!")
goodDay()    


def goodDay(name, ending):
    print("Good Day, " + name)
    print(ending)
    return "ok"
a  = goodDay("Rohan", "Thank you")    
print(a)
b = goodDay("Harry", "Thank you")    
print(b)
c  = goodDay("Shahid", "Thank you")    
print(c)