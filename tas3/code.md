### Case Study 17: Student Performance Trend Analysis

### 1\. Problem Statement

To compare student marks across multiple examinations, calculate improvements or declines, identify weak subjects, and classify student performance.

### 2\. Algorithm

* Store subject names and marks from two examinations.

* Compare the marks of each subject.

* Calculate the difference between the marks.

* If marks increase, display “Improved”.

* If marks decrease, display “Declined”.

* If marks remain the same, display “No Change”.

* Identify subjects with marks below 40 as weak subjects.

* Display the results.

### 3\. Flowchart

mermaid

flowchart TD
    A([Start]) --> B[Store subjects and exam marks]
    B --> C[Read marks for each subject]
    C --> D[Calculate difference between marks]
    D --> E{Difference greater than 0?}
    E -- Yes --> F[Display Improved]
    E -- No --> G{Difference less than 0?}
    G -- Yes --> H[Display Declined]
    G -- No --> I[Display No Change]
    F --> J{Marks below 40?}
    H --> J
    I --> J
    J -- Yes --> K[Display Weak Subject]
    J -- No --> L{More subjects?}
    K --> L
    L -- Yes --> C
    L -- No --> M([End])


### 4\. Python Source Code

python

subjects = ["Python", "Maths", "English"]
exam1 = [60, 35, 70]
exam2 = [75, 30, 70]

for i in range(len(subjects)):
    difference = exam2[i] - exam1[i]

    print("\nSubject:", subjects[i])
    print("Exam 1 Marks:", exam1[i])
    print("Exam 2 Marks:", exam2[i])

    if difference > 0:
        print("Improved by:", difference)
    elif difference < 0:
        print("Declined by:", abs(difference))
    else:
        print("No Change")

    if exam2[i] < 40:
        print("Weak Subject")
    else:
        print("Performance: Good")


### 5\. Sample Input

The program uses these predefined marks:

text
Subjects = Python, Maths, English

Exam 1 = [60, 35, 70]
Exam 2 = [75, 30, 70]


### 6\. Sample Output

text
Subject: Python
Exam 1 Marks: 60
Exam 2 Marks: 75
Improved by: 15
Performance: Good

Subject: Maths
Exam 1 Marks: 35
Exam 2 Marks: 30
Declined by: 5
Weak Subject

Subject: English
Exam 1 Marks: 70
Exam 2 Marks: 70
No Change
Performance: Good


### 7\. Explanation

* Python: 75 − 60 = 15 marks improved.

* Maths: 30 − 35 = −5, so marks declined by 5. Since marks are below 40, it is a weak subject.

* English: Marks remain the same at 70.
