class ClassName:
  
class ClassName:
    # Class attributes (shared by all instances)
    class_attribute = value

class ClassName:
    # Class attributes (shared by all instances)
    class_attribute = value
    # Constructor method (initialize instance attributes)
    def __init__(self, attribute1, attribute2, ...):
        pass
        # ...

class ClassName:
    # Class attributes (shared by all instances)
    class_attribute = value
    # Constructor method (initialize instance attributes)
    def __init__(self, attribute1, attribute2, ...):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        # ...

class ClassName:
    # Class attributes (shared by all instances)
    class_attribute = value
    # Constructor method (initialize instance attributes)
    def __init__(self, attribute1, attribute2, ...):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        # ...
    # Instance methods (functions)
    def method1(self, parameter1, parameter2, ...):
        # Method logic
        pass

  class ClassName:
    # Class attributes (shared by all instances)
    
    class_attribute = value
    # Constructor method (initialize instance attributes)
    def __init__(self, attribute1, attribute2, ...):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        # ...
    # Instance methods (functions)
    def method1(self, parameter1, parameter2, ...):
        # Method logic
        pass
    def method2(self, parameter1, parameter2, ...):
        # Method logic
        pass

CREATING OBJECTS (INSTANCES)
# Create objects (instances) of the class
object1 = ClassName(arg1, arg2, ...)
object2 = ClassName(arg1, arg2, ...)

Method 1: Using dot notation
# Calling methods on objects
# Method 1: Using dot notation
result1 = object1.method1(param1_value, param2_value, ...)
result2 = object2.method2(param1_value, param2_value, ...)

Method 2: Assigning object methods to variables
# Method 2: Assigning object methods to variables
method_reference = object1.method1  # Assign the method to a variable
result3 = method_reference(param1_value, param2_value, ...)

# Method 2: Assigning object methods to variables
method_reference = object1.method1  # Assign the method to a variable
result3 = method_reference(param1_value, param2_value, ...)
# Accessing object attributes
attribute_value = object1.attribute1  # Access the attribute using dot notation

Modifying object attributes
# Modifying object attributes
object1.attribute2 = new_value  # Change the value of an attribute using dot notation

Accessing class attributes (shared by all instances)
# Accessing class attributes (shared by all instances)
class_attr_value = ClassName.class_attribute

Import the library para dibujar circulos
import matplotlib.pyplot as plt
%matplotlib inline 

class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()

  crear una instancia
# Create an object RedCircle

RedCircle = Circle(10, 'red')
# Find out the methods can be used on the object RedCircle

dir(RedCircle)
# Print the object attribute radius

RedCircle.radius
RedCircle.color
# Set the object attribute radius

RedCircle.radius = 1
RedCircle.radius

# Call the method drawCircle

RedCircle.drawCircle()

increase de radius
# Call the method drawCircle

RedCircle.drawCircle()

CREAT METODO PARA MOSTRAR LAS PROPIEDADES
class Vehicle:
    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = None

    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def show_properties(self):
        print("Properties of the car:")
        print("color:", self.color)
        print("Maximum Speed:",self.max_speed)
        print("Mileage:",self.mileage)
        print("seating capacity:",self.seating_capacity)

Creando objeto de carro
class car:
    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = None

    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def show_properties(self):
        print("Properties of the Vehicle:")
        print("Color:", self.color)
        print("Maximum Speed:", self.max_speed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.seating_capacity)

car1=car(200,20)
car1.assign_seating_capacity(5)
car1.show_properties()

car2=car(180,25)
car2.assign_seating_capacity(4)
car2.show_properties()

Implement a code to format the text in lowercase
# Press Shift+Enter to run the code.
class TextAnalzer(object):
    
    def __init__ (self, text):
        # remove punctuation
          formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        
        # make text lowercase
        formattedText = formattedText.lower()
        
        self.fmtText = formattedText

COUNT FREQUENCY
class TextAnalyzer(object):
    
    def __init__ (self, text):
        # remove punctuation
             formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        # make text lowercase
        formattedText = formattedText.lower()
        
        self.fmtText = formattedText
    def freqAll(self):        
        # split text into words
        splited=selffmtText.split(" ")
        # Create dictionary
        freqMap:{}
        for word in set (wordList):
            freqMap[word]=wordlist.count(word)
        return freqMap
