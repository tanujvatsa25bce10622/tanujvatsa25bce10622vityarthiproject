students = []
marks = {}
attendance = {}

while True:
    print("""
    1. Add Student
    2. View Students
    3. Add Marks
    4. View Marks
    5. Mark Attendance
    6. View Attendance
    7. Exit
    """)
    choice = input("Enter your choice: ")

    if choice == '1':
        roll_no = input("Enter Roll Number: ")
        exists = False
        for stu in students:
            if stu['RollNo'] == roll_no:
                exists = True
                break
        if exists:
            print("Student already exists.")
        else:
            name = input("Enter Name: ")
            branch = input("Enter Branch: ")
            students.append({'RollNo': roll_no, 'Name': name, 'Branch': branch})
            print("Student added successfully.")

    elif choice == '2':
        if len(students) == 0:
            print("No students added yet.")
        else:
            for stu in students:
                print(stu['RollNo'], stu['Name'], stu['Branch'])

    elif choice == '3':
        roll_no = input("Enter Roll Number: ")
        found = False
        for stu in students:
            if stu['RollNo'] == roll_no:
                found = True
        if not found:
            print("Student not found.")
        else:
            subject = input("Enter Subject: ")
            mark = input("Enter Marks: ")
            try:
                mark = int(mark)
            except:
                print("Enter marks as a number.")
                continue
            if roll_no not in marks:
                marks[roll_no] = {}
            marks[roll_no][subject] = mark
            print("Marks added.")

    elif choice == '4':
        roll_no = input("Enter Roll Number: ")
        found = False
        for stu in students:
            if stu['RollNo'] == roll_no:
                found = True
        if not found:
            print("Student not found.")
        elif roll_no not in marks or len(marks[roll_no]) == 0:
            print("No marks recorded.")
        else:
            print("Marks for", roll_no)
            for subject in marks[roll_no]:
                print(subject, marks[roll_no][subject])

    elif choice == '5':
        roll_no = input("Enter Roll Number: ")
        found = False
        for stu in students:
            if stu['RollNo'] == roll_no:
                found = True
        if not found:
            print("Student not found.")
        else:
            if roll_no in attendance:
                attendance[roll_no] += 1
            else:
                attendance[roll_no] = 1
            print("Attendance marked.")

    elif choice == '6':
        roll_no = input("Enter Roll Number: ")
        found = False
        for stu in students:
            if stu['RollNo'] == roll_no:
                found = True
        if not found:
            print("Student not found.")
        else:
            att_count = attendance.get(roll_no, 0)
            print("Attendance for", roll_no, ":", att_count, "days")

    elif choice == '7':
        print("Exiting program.")
        break

    else:
        print("Invalid choice, please try again.")
