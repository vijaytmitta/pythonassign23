#Create a function that returns the mean of all digits.
import math
def mean(x):
    x=str(x)
    sum_x=0
    for i in x:
        sum_x+=int(i)
    mean=sum_x/len(x)
    return print(mean)

mean(42)
mean(12345)
mean(666)