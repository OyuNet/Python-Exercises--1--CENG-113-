distance = 840
firstVelocity = 50
secondVelocity = 70
hour = 0

while (True):
    totalVelocity = firstVelocity + secondVelocity
    distance = distance - totalVelocity
    hour = hour + 1
    
    if (distance == 240):
        break
    
    
print("It takes",hour,"hour")
    