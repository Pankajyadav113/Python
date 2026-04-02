a = (1, 2, 3,  4, ) # Tuple                    
                    # Tuple is immutable
print(type(a))

a = ()              # Empty tuple
print(type(a))

a = (1,)            # a tuple which have only one element
print(type(a))

# Tuple methods
a = (1, 45,342, 3424,False, "Rohan")
print(a)
no = a.count(45)
print(no)

i = a.index(3424)
print(i)

# Concatenation  

tuple1 = (1, 2, 3, 4, )
tuple2 = ( 4, 5, 6, 7 )
concaneted = tuple1 + tuple2
print(concaneted)

# Repeation of tuple 

my_tuple = (1, 2, 3, 4)
repeated = my_tuple*3
print(repeated)

# Check an item existsnin s tuple or not

my_tuple = ( 12, 34, 45, 55 , 23)
print( 2 in my_tuple)                # Output :  False                           
print(12 in my_tuple)                # Output :  True

# Length of a tuple 

tuple = ( 1, 2,3 ,4, 334, 4334,)
print(len(tuple))                    # Output :  6

# Smallest and largest element of a tuple

tuple =  (123, 34, 4,54,56,6,2,56,6)
print(min(tuple))                   # Output :  2
print(max(tuple))                   # Output :  123                

# Slicing of a tuple 

my_tuple =  ( 1, 3, 4,6,7,8 )
sliced = my_tuple[1:4]
print(sliced)                       # output :  (3, 4, 6)

# Unpacking : Tuple can be unpack into individual variable

my_tuple = (1,2,3,)
a,b,c = my_tuple
print(a,b,c)                        # Output :  1 2 3

