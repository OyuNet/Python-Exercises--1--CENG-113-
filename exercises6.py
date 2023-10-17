import math

print("Enter the side lengths of right angle.")

firstSide = float(input("Enter the first length: "))
secondSide = float(input("Enter the second length: "))

hypotenuse = float(math.sqrt(firstSide**2 + secondSide**2))

print("Your desired hypotenuse is", hypotenuse)