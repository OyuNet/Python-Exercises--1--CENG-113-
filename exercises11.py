givenTime = int(input("Enter seconds: "))

convDay = givenTime // 86400
convHour = (givenTime-convDay*86400) // 3600
convMin = (givenTime-convDay*86400-convHour*3600) // 60
convSec = (givenTime-convDay*86400-convHour*3600-convMin*60)
    
print("{total} seconds = {day} day(s) {hour} hour(s) {min} minute(s) {sec} second(s)".format(total = givenTime, day = convDay, hour = convHour, min = convMin, sec = convSec))