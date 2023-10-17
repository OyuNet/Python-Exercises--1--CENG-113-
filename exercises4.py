def celciusToFahrenheit(celciusDegree):
    celciusDegree = float(celciusDegree)
    fahrenheitDegree = float(celciusDegree*(9/5)+32)
    return fahrenheitDegree

value = float(input("Enter your Celcius degree: "))
response = celciusToFahrenheit(value)

print("Weather is",response,"fahrenheit.")
