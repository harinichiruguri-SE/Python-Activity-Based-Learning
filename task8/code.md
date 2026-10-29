### Case Study 22: Laboratory Chemical Inventory Validation

### 1\. Problem Statement

To check the quantity of chemicals in a laboratory. If a chemical's quantity exceeds the maximum limit of 10, the program displays an invalid message. It also displays the storage category of each chemical.

### 2\. Algorithm

* Start.

* Store the chemical name, category, and quantity.

* Set the maximum quantity to 10.

* Check each chemical's quantity.

* If the quantity exceeds 10, display an invalid message.

* Otherwise, display that the quantity is within the limit.

* Display the storage category.

* Stop.

### 3\. Flowchart

mermaid

flowchart TD
    A([Start]) --> B[Store chemical details]
    B --> C[Set maximum quantity to 10]
    C --> D[Read chemical details]
    D --> E[Display chemical name]
    E --> F{Quantity > 10?}
    F -- Yes --> G[Display Invalid: Quantity exceeds limit]
    F -- No --> H[Display Quantity is within limit]
    G --> I[Display storage category]
    H --> I
    I --> J{More chemicals?}
    J -- Yes --> D
    J -- No --> K([Stop])


### 4\. Python Source Code

python

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


### 5\. Sample Input

The chemical details are already given in the program:

* Chemical A — Acid — Quantity 5

* Chemical B — Base — Quantity 8

* Chemical C — Acid — Quantity 15

Maximum quantity = 10.

### 6\. Sample Output

text

Chemical: Chemical A
Quantity is within limit
Storage category: Acid
Chemical: Chemical B
Quantity is within limit
Storage category: Base
Chemical: Chemical C
Invalid: Quantity exceeds limit
Storage category: Acid


### 7\. Explanation

* The program checks each chemical one by one.

* Chemical A has quantity 5, which is within the limit.

* Chemical B has quantity 8, which is within the limit.

* Chemical C has quantity 15, which exceeds the limit of 10.

* Therefore, Chemical C is marked as invalid.

* The storage category is displayed for every chemical.
