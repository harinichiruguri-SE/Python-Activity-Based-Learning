#case study 20:University Admission Decision Engine
students = [
    ("A", 85, 80),
    ("B", 75, 70),
    ("C", 90, 90),
    ("D", 60, 65)
]

eligible = []

for name, aggregate, subject_marks in students:
    if aggregate >= 70 and subject_marks >= 60:
        eligible.append((name, aggregate, subject_marks))

eligible.sort(key=lambda x: (x[1], x[2]), reverse=True)

print("Eligible Students Ranked:")

rank = 1
for name, aggregate, subject_marks in eligible:
    print(rank, name, aggregate, subject_marks)
    rank += 1
