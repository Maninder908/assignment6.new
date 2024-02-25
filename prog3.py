def convert_to_liters(gallons):
    liters = gallons * 5.21189
    return liters


while True:
    gallons = float(input("How many gallons of gasoline do you have? (Enter a negative value to exit): "))

    if gallons < 0:
        print("Exiting the program...")
        break

    liters = convert_to_liters(gallons)
    print("You have", liters, "liters of gasoline.")