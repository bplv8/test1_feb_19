'''Q2. Create a class Circle which has a class variable PI with the value=22/7.
Make two methods getArea and getCircumference inside this Circle class. Which when
invoked returns area and circumference of each circle instances.'''

import cmath
class Circle:
 PI=22/7
 def __init__(self,r):
   self.r= r

 def getArea(self):
   return Circle.PI*self.r*self.r

 def getCircumference(self):
  return 2*Circle.PI*self.r

obj=Circle(3)
print("The area is:",obj.getArea())
print("The circumferene is:",obj.getCircumference())