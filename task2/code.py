# Case 16: Multi day Water tank Simulation 
capacity = 1000
level = 500
threshold = 800

inflow = [200, 300, 100, 250]
outflow = [100, 150, 200, 100]

for i in range(len(inflow)):
    level = level + inflow[i] - outflow[i]

    print("Day", i + 1)
    print("Water Level:", level)

    if level > capacity:
        print("Overflow detected")
        level = capacity
    elif level < 0:
        print("Water shortage")
        level = 0

    if level >= threshold:
        print("Threshold reached")
        break
