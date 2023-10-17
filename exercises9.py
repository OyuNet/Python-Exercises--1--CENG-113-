import math

radius = float(input("Enter your radius: "))

circleArea = math.pi*(radius**2)
circumference = 2*math.pi*radius

smallestSquare = math.sqrt(((2*radius)**2)/2)
biggestSquare = (2*radius)**2

print("Circle Area is",circleArea)
print("Circle Circumference is",circumference)
print("Smallest Square is",smallestSquare)
print("Biggest Square is", biggestSquare)