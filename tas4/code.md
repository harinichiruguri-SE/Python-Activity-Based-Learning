### Case Study 18: Fuel Consumption and Route Comparison

### 1\. Problem Statement

To calculate the fuel required and journey cost for different vehicles based on distance, mileage, fuel price, and reserve fuel. Identify the vehicle with the lowest journey cost.

### 2\. Algorithm

* Store vehicle names and their mileage values.

* Set the journey distance, fuel price, and reserve fuel.

* Calculate fuel required using distance divided by mileage.

* Add reserve fuel to the calculated fuel.

* Calculate the journey cost by multiplying required fuel by fuel price.

* Compare the costs of all vehicles.

* Display the vehicle with the lowest cost.

### 3\. Flowchart

mermaid

flowchart TD
    A([Start]) --> B[Set vehicles, distance, price and reserve]
    B --> C[Set lowest cost = None]
    C --> D[Calculate fuel = distance / mileage]
    D --> E[Add reserve fuel]
    E --> F[Calculate journey cost]
    F --> G[Display fuel and cost]
    G --> H{Is cost lower than lowest cost?}
    H -- Yes --> I[Update lowest cost and best vehicle]
    H -- No --> J{More vehicles?}
    I --> J
    J -- Yes --> D
    J -- No --> K[Display lowest-cost vehicle and cost]
    K --> L([End])


### 4\. Python Source Code

python

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


### 5\. Sample Input

The program uses these predefined values:

text
Distance = 200 km
Fuel price = ₹100 per litre
Reserve fuel = 2 litres

Car mileage = 15 km/litre
Bike mileage = 40 km/litre
Bus mileage = 5 km/litre


### 6\. Sample Output

text

Car
Fuel required: 15.333333333333334
Journey cost: 1533.3333333333335
Bike
Fuel required: 7.0
Journey cost: 700.0
Bus
Fuel required: 42.0
Journey cost: 4200.0
Lowest-cost vehicle: Bike
Minimum cost: 700.0


### 7\. Explanation

* Car: litres. Cost = ₹1,533.33.

* Bike: litres. Cost = ₹700.

* Bus: litres. Cost = ₹4,200.

* The bike has the lowest journey cost of ₹700.
