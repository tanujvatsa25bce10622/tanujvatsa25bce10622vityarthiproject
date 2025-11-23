students = []
attendance = {}

while True:
    print("=== MENU ===")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Mark Attendance")
    print("4. Show Attendance")
    print("5. Exit")
    ch = input("Choose option: ")

    if ch == "1":
        rno = input("Enter Roll Number: ")
        found = False
        for s in students:
            if s["rno"] == rno:
                found = True
        if found:
            print("Already exists!")
        else:
            name = input("Enter Name: ")
            branch = input("Enter Branch: ")
            students.append({"rno": rno, "name": name, "branch": branch})
            print("Student added.")

    elif ch == "2":
        if len(students) == 0:
            print("No students yet.")
        for s in students:
            print(s["rno"], s["name"], s["branch"])

    elif ch == "3":
        rno = input("Enter Roll Number: ")
        found = False
        for s in students:
            if s["rno"] == rno:
                found = True
        if not found:
            print("Student not found.")
        else:
            if rno in attendance:
                attendance[rno] += 1
            else:
                attendance[rno] = 1
            print("Attendance marked.")

    elif ch == "4":
        rno = input("Enter Roll Number: ")
        if rno in attendance:
            print("Attendance for", rno, ":", attendance[rno])
        else:
            print("No attendance found.")

    elif ch == "5":
        print("Bye!")
        break

    else:
        print("Invalid choice!")
