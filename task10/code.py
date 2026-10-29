#case study 24:Courier Charge Optimization
weight = float(input("Enter parcel weight in kg: "))
distance = float(input("Enter distance in km: "))
urgent = input("Urgent delivery? (yes/no): ").lower()

if weight <= 0 or distance <= 0:
    print("Invalid parcel details")
else:
    standard = 50 + weight * 10 + distance * 2
    express = 100 + weight * 15 + distance * 3

    if urgent == "yes":
        print("Selected service: Express")
        print("Courier charge:", express)
    else:
        if standard <= express:
            print("Selected service: Standard")
            print("Courier charge:", standard)
        else:
            print("Selected service: Express")
            print("Courier charge:", express)
