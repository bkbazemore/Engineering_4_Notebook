import math
import array as arr

print("Quadratic Solver: Enter the coefficients for ax^2 + bx + c = 0")

def doQuad(a,b,c):
    d=(b**2) - (4*a*c)
   
    if d < 0:
        print ("this equation has no real solutions")
        arr = []
    elif d == 0:
        x = (-b+math.sqrt(d))/(2*a)
        print("This equation has one solution:  ", x)
        arr = [x]
    else:
        x1 = (-b+math.sqrt(d))/(2*a)
        x2 = (-b-math.sqrt(d))/(2*a)
        print("This equation has 2 solutions: ", x1, "or", x2)
        arr = [x1,x2]
    return arr
    
number_1 = input('Enter A: ')
number_2 = input('Enter B: ')
number_3 = input('Enter C: ')
a = int(number_1)
b = int(number_2)
c = int(number_3)

return1 = doQuad(a,b,c) 

print(return1)

