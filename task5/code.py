#case study 19: Multi-Product Shopping Budget Constraint
products = ["Shirt", "Shoes", "Bag"]
prices = [500, 1500, 800]
quantities = [2, 1, 2]
budget = 2500
total = 0
for i in range(len(products)):
    cost = prices[i] * quantities[i]
    total += cost
    print(products[i], "Cost:", cost)
print("Total cost:", total)
for i in range(len(products)):
    while total > budget and quantities[i] > 0:
        quantities[i] -= 1
        total -= prices[i]
print("\nFinal shopping list:")
for i in range(len(products)):
    print(products[i], "Quantity:", quantities[i])
print("Final total:", total)
print("Remaining budget:", budget - total)
