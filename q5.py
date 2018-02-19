'''Define an Student class and initialize it with name and section.
Now, make a classmethod that takes in a string parameter "name-A" which creates an instance and
returns the instance based on parameter.
[Hint: use @classmethod decorator]'''

class Student(object):
 def __init__(self,name,section):
  self.name = name
  self.section = section

 @classmethod
 def get_str_from_string(cls,inp):
  name, section = (inp.split("-"))
  return cls(name, section)

str = Student.get_str_from_string("name-A")
print(str.__dict__)