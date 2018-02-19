''' Create a Temperature class. Make two methods :
a. convertFahrenheit - It will take Celsius and will print it into Fahrenheit.
b. convertCelsius - It will take Fahrenheit and will convert it into Celsius.'''


class Temperature(object):
 def convertFahrenheit(Celsius):
  print("Celcius = {}\nFahrenhiet = {}".format(Celsius, 1.8 * Celsius + 32))

 def convertCelcius(Fahrenheit):
   print("Fahrenheit = {}\nCelcius = {}".format(Fahrenheit, (Fahrenheit - 32) / 1.8))

temp = Temperature
temp.convertFahrenheit(10.5)
temp.convertCelcius(30.6)