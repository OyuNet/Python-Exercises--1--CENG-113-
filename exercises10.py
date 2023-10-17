value = int(input("Enter your number between 0 and 10000: "))

array = []

for letter in str(value): # Now we are splitting letters, appending into JSON array.
    array.append(letter)
    
arrayLen = len(array)
indexNum = 0

while (indexNum < arrayLen):
    print("Your {current}. number is {num}".format(current = indexNum + 1, num = array[arrayLen-indexNum-1]))
    indexNum = indexNum + 1