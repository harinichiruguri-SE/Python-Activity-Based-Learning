#case study 22:Laboratory Chemical Inventory Validation
chemicals = [
    ("Chemical A", "Acid", 5),
    ("Chemical B", "Base", 8),
    ("Chemical C", "Acid", 15)
]

max_quantity = 10

for name, category, quantity in chemicals:
    print("Chemical:", name)

    if quantity > max_quantity:
        print("Invalid: Quantity exceeds limit")
    else:
        print("Quantity is within limit")

    print("Storage category:", category)
