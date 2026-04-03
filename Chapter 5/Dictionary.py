# It is unorderable 
# It is mutable
# It is indexed
# Cannot contaion duplicate value


# marks = {
#     "Harry": 100,
#     "Rohan":23,
# }
# print(marks["Harry"])

#  Method of dictonary

marks = {
    "Harry": 100,
    "Rohan":23,
    0: "Harry"
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Harry":99, "Renuka": 100}) # Update method
print(marks)
print(marks.get("Harry"))                #  Prints None
print(marks["Harry"])                    # Returns an error
d = {}                                   # Empty dictonary
