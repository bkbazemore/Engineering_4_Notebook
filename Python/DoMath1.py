import math 

def doMath(a,b,c):
    a=int(a)
    b=int(b)
    if c == 1:
        return str(a+b) 
    else:
        if c == 2:
            return str(a-b)
    
        if c == 3:
            return str(a*b)
    
        if c == 4:
            return  str(round((a/b),2))
    
        if c == 5:
            return str(a%b)


number_1 = input('Enter your first number: ')
number_2 = input(' Enter your second number: ')
a = number_1
b = number_2
    

print("Sum:\t\t " + doMath(a,b,1))
print("Differnce:\t" + doMath(a,b,2))
print("Product:\t" + doMath(a,b,3))
print("Quotient:\t " + doMath(a,b,4))
print(" Modulo:\t\t" + doMath(a,b,5))
