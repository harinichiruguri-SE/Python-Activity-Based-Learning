### Case Study 16: Multi-Day Water Tank Simulation

### 1\. Problem Statement

To calculate the water level in a tank by adding inflow and subtracting outflow each day. The program checks for overflow and water shortage and identifies the first day the water level reaches a specified threshold.

### 2\. Algorithm

* Set the initial water level, tank capacity, and threshold.

* Store daily inflow and outflow values in lists.

* Calculate the new water level by adding inflow and subtracting outflow.

* Display the water level for each day.

* If the water level exceeds capacity, display “Overflow”.

* If the water level is below zero, display “Water Shortage”.

* If the water level reaches the threshold, display the day and stop the loop.

### 3\. Flowchart

mermaid

flowchart TD
    A([Start]) --> B[Set initial level, capacity and threshold]
    B --> C[Store inflow and outflow lists]
    C --> D[Calculate new water level]
    D --> E[Display day and water level]
    E --> F{Level greater than capacity?}
    F -- Yes --> G[Display Overflow]
    F -- No --> H{Level less than 0?}
    G --> I{Level reaches threshold?}
    H -- Yes --> J[Display Water Shortage]
    H -- No --> I
    J --> I
    I -- Yes --> K[Display threshold day and stop]
    I -- No --> L{More days?}
    L -- Yes --> D
    L -- No --> M([End])
    K --> M


### 4\. Python Source Code

python

level = 500
capacity = 1000
threshold = 800

inflow = [200, 300, 100, 250]
outflow = [100, 150, 200, 100]

for i in range(4):
    level = level + inflow[i] - outflow[i]

    print("Day", i + 1, "Water Level:", level)

    if level > capacity:
        print("Overflow")
    elif level < 0:
        print("Water Shortage")

    if level >= threshold:
        print("Threshold Reached on Day", i + 1)
        break


### 5\. Sample Input

The program uses these predefined values:

text
Initial water level = 500 litres
Tank capacity = 1000 litres
Threshold = 800 litres

Inflow = [200, 300, 100, 250]
Outflow = [100, 150, 200, 100]


### 6\. Sample Output

text
Day 1 Water Level: 600
Day 2 Water Level: 750
Day 3 Water Level: 650
Day 4 Water Level: 800
Threshold Reached on Day 4


### 7\. Explanation

* Initial water level = 500 litres.

* Day 1: 500 + 200 − 100 = 600 litres.

* Day 2: 600 + 300 − 150 = 750 litres.

* Day 3: 750 + 100 − 200 = 650 litres.

* Day 4: 650 + 250 − 100 = 800 litres.

* The threshold is 800 litres, so it is reached on Day 4.
