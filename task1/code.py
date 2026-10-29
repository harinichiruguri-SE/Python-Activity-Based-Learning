#case study 15:Smart Parking Fee Management
hours = float(input("Enter parking hours: "))
vehicle = input("Enter vehicle type (car/bike): ").lower()
if hours <= 0:
    print("Invalid parking hours")
else:
    if vehicle == "car":
        rate = 30
    elif vehicle == "bike":
        rate = 15
    else:
        rate = 0

    if rate == 0:
        print("Invalid vehicle type")
    else:
        fee = hours * rate

        if hours > 24:
            fee += 100

        print("Parking fee:", fee)
