#Program to create a patient appointment scheduling system with time conflict validation and cancellation feature.
schedule = []

# BOOK APPOINTMENTS
while True:
    n = input("Enter patient name: ")
    s = float(input("Start time: "))
    e = float(input("End time: "))

    conflict = False
    for appt in schedule:
        if s < appt[2] and e > appt[1]:
            print("Time conflict with", appt[0])
            conflict = True
            break

    if not conflict:
        schedule.append([n, s, e])
        print("Appointment booked")

    if input("Add more patients? (yes/no): ") != "yes":
        break

# MENU
while True:
    print("\n1) Cancel appointment")
    print("2) Show all")
    print("3) Exit")

    ch = input("Choose: ")

    if ch == "1":
        name_n = input("Enter patient name: ")

        for appt in schedule:
            if appt[0] == name_n:
                schedule.remove(appt)
                print("Appointment cancelled")
                break
        else:
            print("Name does not exist")

    elif ch == "2":
        print("Schedule:", schedule)

    elif ch == "3":
        break

