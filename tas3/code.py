#Case 17: Students perform Analysis 
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
