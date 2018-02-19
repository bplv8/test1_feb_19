"""Q1. Create a RectangleGeometry class which takes in length and breadth as initialize parameter.
Make two methods getArea and getPerimeter inside this class. Which when invoked returns area and perimeter of
each rectangle instance."""

import cmath
class RectangleGeometry():
 def __init__(self, breadth, length):
  self.breadth = b
  self.length = l

 def getArea(self):
  return self.breadth * self.length

 def getPerimeter(self):
  return 2*(self.breadth + self.length)



l = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))
obj = RectangleGeometry(l,b)
print("Area of rectangle:", obj.getArea())

print("Perimeter of rectangle",obj.getPerimeter())