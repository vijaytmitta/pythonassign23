#Create a function that takes a number as an argument and returns True or False depending on whether the number
# is symmetrical or not. A number is symmetrical when it is the same as its reverse.


def is_symmetrical(number):
    return print(str(number) == str(number)[::-1])


is_symmetrical(7227)
is_symmetrical(12567)
is_symmetrical(44444444)
is_symmetrical(9939)
is_symmetrical(1112111)
