#case study 23:Student Timetable Conflict Dettection
timetable = [
    ("Python", "9-10", "Room A"),
    ("Maths", "10-11", "Room B"),
    ("English", "9-10", "Room A"),
    ("Physics", "11-12", "Room C")
]

for i in range(len(timetable)):
    for j in range(i + 1, len(timetable)):
        course1, time1, room1 = timetable[i]
        course2, time2, room2 = timetable[j]

        if time1 == time2:
            print("Time conflict:", course1, "and", course2)

            if room1 == room2:
                print("Room conflict:", room1)

print("Timetable checking completed")
