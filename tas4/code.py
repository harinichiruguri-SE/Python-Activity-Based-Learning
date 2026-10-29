#case study 18:Fuel Consumption and Route Comparision
vehicles = ["Car", "Bike", "Bus"]
distance = 200
fuel_price = 100
reserve = 2
mileage = [15, 40, 5]
lowest_cost = None
best_vehicle = ""
for i in range(len(vehicles)):
    fuel = distance / mileage[i]
    required_fuel = fuel + reserve
    cost = required_fuel * fuel_price

    print(vehicles[i])
    print("Fuel required:", required_fuel)
    print("Journey cost:", cost)
    if lowest_cost is None or cost < lowest_cost:
        lowest_cost = cost
        best_vehicle = vehicles[i]
print("Lowest-cost vehicle:", best_vehicle)
print("Minimum cost:", lowest_cost)
