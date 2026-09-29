
def main():

    students = []

    while True:

        print("\n==========================================")
        print("       STUDENT DATA ORGANIZER")
        print("==========================================")

        print("\n1. Add Student")
        print("2. Display All Students")
        print("3. Update Student Information")
        print("4. Delete Student")
        print("5. Display Subjects Offered")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            display_students(students)

        elif choice == "3":
            update_student(students)

        elif choice == "4":
            delete_student(students)

        elif choice == "5":
            display_subjects(students)

        elif choice == "6":
            print("\nThank you for using Student Data Organizer!")
            print("Program exited successfully.")
            break

        else:
            print("\nInvalid choice. Please try again.")

# ADD STUDENT

def add_student(students):

    print("\n--- Add Student ---")

    student_id = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    grade = input("Enter Grade: ")
    dob = input("Enter Date of Birth (YYYY-MM-DD): ")

    subject_input = input("Enter Subjects (comma-separated): ")

    subjects = set()

    for subject in subject_input.split(","):
        subjects.add(subject.strip())

    personal_info = (student_id, dob)

    student = {
        "personal_info": personal_info,
        "name": name,
        "age": age,
        "grade": grade,
        "subjects": subjects
    }

    students.append(student)

    print("\nStudent added successfully!")

# DISPLAY STUDENTS

def display_students(students):

    print("\n--- Display All Students ---")

    if len(students) == 0:
        print("No student records found.")
        return

    for student in students:

        student_id, dob = student["personal_info"]

        subjects = ", ".join(sorted(student["subjects"]))

        print(
            f"\nStudent ID: {student_id}"
            f"\nName: {student['name']}"
            f"\nAge: {student['age']}"
            f"\nGrade: {student['grade']}"
            f"\nDate of Birth: {dob}"
            f"\nSubjects: {subjects}"
        )
# UPDATE STUDENT

def update_student(students):

    print("\n--- Update Student Information ---")

    student_id = int(input("Enter Student ID to update: "))

    for student in students:

        if student["personal_info"][0] == student_id:

            print("\n1. Update Name")
            print("2. Update Age")
            print("3. Update Grade")
            print("4. Update Subjects")

            choice = input("Enter your choice: ")

            if choice == "1":

                student["name"] = input("Enter new name: ")
                print("Name updated successfully.")

            elif choice == "2":

                student["age"] = int(input("Enter new age: "))
                print("Age updated successfully.")

            elif choice == "3":

                student["grade"] = input("Enter new grade: ")
                print("Grade updated successfully.")

            elif choice == "4":

                subject_input = input(
                    "Enter new Subjects (comma-separated): "
                )

                new_subjects = set()

                for subject in subject_input.split(","):
                    new_subjects.add(subject.strip())

                student["subjects"] = new_subjects

                print("Subjects updated successfully.")

            else:
                print("Invalid choice.")

            return

    print("Student ID not found.")

# DELETE STUDENT

def delete_student(students):

    print("\n--- Delete Student ---")

    student_id = int(input("Enter Student ID to delete: "))

    for i in range(len(students)):

        if students[i]["personal_info"][0] == student_id:

            del students[i]

            print("Student deleted successfully.")
            return

    print("Student ID not found.")

# DISPLAY UNIQUE SUBJECTS

def display_subjects(students):

    print("\n--- Subjects Offered ---")

    all_subjects = set()

    for student in students:
        all_subjects.update(student["subjects"])

    if len(all_subjects) == 0:
        print("No subjects found.")
        return

    print("\nUnique Subjects:")

    for subject in sorted(all_subjects):
        print("-", subject)


main()
