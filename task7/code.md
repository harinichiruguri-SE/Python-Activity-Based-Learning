### Case Study 21: Traffic Violation Penalty Calculator

### 1\. Problem Statement

To calculate traffic fines based on violations. If a person repeats a violation, the fine is doubled. If the total fine is ₹3000 or more, the program displays a warning for possible disqualification.

### 2\. Algorithm

* Start.

* Store the fine amount for each violation.

* Store the list of violations and whether each is repeated.

* Set total_fine = 0.

* Check each violation.

* If it is repeated, double the fine.

* Display each fine and add it to the total.

* Display the total penalty.

* If the total is ₹3000 or more, display a disqualification warning.

* Stop.

### 3\. Flowchart

mermaid

flowchart TD
    A([Start]) --> B[Store fine rules and violations]
    B --> C[Set total fine to 0]
    C --> D[Check each violation]
    D --> E{Is offence known?}
    E -- No --> F[Display unknown offence]
    E -- Yes --> G[Get fine amount]
    G --> H{Repeated violation?}
    H -- Yes --> I[Double the fine]
    H -- No --> J[Keep original fine]
    I --> K[Display fine and add to total]
    J --> K
    F --> L{More violations?}
    K --> L
    L -- Yes --> D
    L -- No --> M[Display total penalty]
    M --> N{Total fine >= 3000?}
    N -- Yes --> O[Display disqualification warning]
    N -- No --> P([Stop])
    O --> P


### 4\. Python Source Code

python

fine_rules = {
    "helmet": 500,
    "overspeeding": 1000,
    "signal": 1500
}

violations = [
    ("helmet", False),
    ("overspeeding", True),
    ("signal", False)
]

total_fine = 0

for offence, repeat in violations:
    if offence in fine_rules:
        fine = fine_rules[offence]

        if repeat:
            fine *= 2

        print(offence, "Fine:", fine)
        total_fine += fine
    else:
        print("Unknown offence:", offence)

print("Total penalty:", total_fine)

if total_fine >= 3000:
    print("Review for possible disqualification")


### 5\. Sample Input

The values are already given in the program:

* Helmet violation — not repeated

* Overspeeding — repeated

* Signal violation — not repeated

### 6\. Sample Output

text

helmet Fine: 500
overspeeding Fine: 2000
signal Fine: 1500
Total penalty: 4000
Review for possible disqualification


### 7\. Explanation

* The program stores the fine amounts in a dictionary.

* The helmet fine is ₹500 because it is not repeated.

* The overspeeding fine becomes ₹2000 because it is repeated.

* The signal fine is ₹1500.

* The total penalty is ₹4000.

* Since the total is greater than ₹3000, the program displays the warning.
