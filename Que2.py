#Given a string of numbers separated by a comma and space, return the product of the numbers.
def multiply_nums(lis):
    prodt=1
    lis=list(lis.split())
    for i in range(len(lis)):
        prodt=prodt*int(lis[i].strip(","))
    return print(prodt)


multiply_nums("2, 3")
multiply_nums("1, 2, 3, 4")
multiply_nums("54, 75, 453, 0")
multiply_nums("10, -2")