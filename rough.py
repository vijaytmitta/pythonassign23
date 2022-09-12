app=("2, 3")
import math
print(int(app[0])*int(app[3]))
print((list(app)))
print(list(app.replace(",","")))
print(list(app.split(",")))
#print(list(app.split(" ")))
print(list(("54, 75, 453, 10").replace(",","")))
print(list(("54, 75,  453, -10").split())[0].strip(","))
a=[2,3,1]
print(list(set([1, 3, 3, 5, 5])))