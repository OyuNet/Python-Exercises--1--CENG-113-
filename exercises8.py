import math

firstRadius = float(input("Enter your first radius: "))
secondRadius = float(input("Enter your second radius: "))

bigRadius = (firstRadius+secondRadius)

firstArea = math.pi*(firstRadius**2)
secondArea = math.pi*(secondRadius**2)
bigArea = math.pi*(bigRadius**2)

leftArea = bigArea-firstArea-secondArea

print("Your left area is", leftArea)