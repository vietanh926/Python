import math 

def solve_quadratic(a,b,c):
    if a == 0: 
        x = -c/b
        return (x , None)
    else: 
        delta = b**2 - 4*a*c
        if delta < 0:
            return None
        if delta == 0:
            x1 = - (b)/(2*a)
            return (x1 , None)
        else: 
            x1 = -(b+math.sqrt(delta))/(2*a)
            x2 = -(b-math.sqrt(delta))/(2*a)
            return (x2,x1)



print(solve_quadratic(0.5,-1.5,1))


