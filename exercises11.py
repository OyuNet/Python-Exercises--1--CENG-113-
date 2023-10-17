givenTime = int(input("Enter seconds: "))

storeTime = givenTime

convDay = 0
convHour = 0
convMin = 0

while (givenTime > 86400):
    givenTime = givenTime-86400
    convDay = convDay + 1
    
while (givenTime > 3600):
    givenTime = givenTime-3600
    convHour = convHour + 1
    
while (givenTime > 60):
    givenTime = givenTime-60
    convMin = convMin + 1
    
print("{total} seconds = {day} day(s) {hour} hour(s) {min} minute(s) {sec} second(s)".format(total = storeTime, day = convDay, hour = convHour, min = convMin, sec = givenTime))