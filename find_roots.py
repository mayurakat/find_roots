import math  

def roots(a,b,c):
    d = (b**2) - (4*a*c)  
  
    sol1 = (-b-math.sqrt(d))/(2*a)  
    sol2 = (-b+math.sqrt(d))/(2*a)
    
    return (sol1,sol2)


a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))  

z = roots(a,b,c)
print(z)