#case study 21:Trafic Violation Penallty Calculator
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
