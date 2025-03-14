from math import sqrt
import copy 
#from World import World  

class Point:
    """"represents a point in a 2D space"""


print(Point)
blank = Point()
print(blank)

blank.x = 3.0
blank.y = 4.0 
print('(%g,%g)'% (blank.x,blank.y))
def printPoint(p):
    print('(%g,%g)'% (p.x,p.y))
    
    
printPoint(blank)

def distance(p,d):
    d = sqrt(p.x**2+p.y**2) + sqrt(d.x**2 + d.y**2)
    print(d)

blank2 = Point()
blank2.x = 4
blank2.y = 6

distance(blank,blank2)
class Rectangle:
    """Represent a rectangle
    attribute : width , height , corner
    """

box = Rectangle()
box.width = 100
box.height = 200
box.corner = Point()
box.corner.x = 0
box.corner.y = 0 

box2 = copy.deepcopy(box)
print(box2 is box)
print(box2.corner is box.corner)

class Circle:
    """Just a class have atribute 
    location = () 
    r = int         """

O = Circle()
O.x  = (150,100)
O.r = 75

def point_in_circle(point,circle):
     pass

def rect_in_circle():
    pass
def rect_in_circle_overlap():
    pass 