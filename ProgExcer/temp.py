def convert_temp():
    f = int(input("Enter the temperature in Fahrenheit: "))
    print(f"The temperature in Fahrenheit is: {f}")
    print(f"The temperature in Celcius is: {(f-32) * 5 / 9}")
    print(f"The temperature in Kelvin is: {(f-32) * 5 / 9 + 273.15}")
convert_temp()


