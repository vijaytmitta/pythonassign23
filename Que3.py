#Create a function that squares every digit of a number.
import math


def square_digits(x):
    x=str(x)
    sd=[]
    for i in range(len(x)):
        sd.append(int(x[i])**2)
    print(*sd, sep="")
    return

square_digits(9119)
square_digits(2483)
square_digits(3212)