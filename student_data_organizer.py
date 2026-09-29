# ============================================
# Project: Collection Manipulator
# Student Data Organizer
# ============================================

students = []


# --------------------------------------------
# Function to Add Student
# --------------------------------------------
def add_student():
    print("\n--- Add Student ---")

    student_id = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    grade = input("Enter Grade: ")
    dob = input("Enter Date of Birth (YYYY-MM-DD): ")

    subject_input = input("Enter Subjects (comma-separated): ")

    # Set is used to store unique subjects
    subjects = set()

    for subject in subject_input.split(","):
        subjects.add(subject.strip())

    # Tuple stores Student ID and Date of Birth
    # Tuple is immutable
    personal_info = (student_id, dob)

    # Dictionary stores complete student information
    student = {
        "personal_info": personal_info,
        "name": name,
        "age": age,
        "grade": grade,
        "subjects": subjects
    }

    # List stores multiple student records
    students.append(student)

    print("\nStudent added successfully!")


# --------------------------------------------
# Function to Display All Students
# --------------------------------------------
def display_students():
    print("\n--- Display All Students ---")

    if len(students) == 0:
        print("No student records found.")
        return

    for student in students:

        student_id, dob = student["personal_info"]

        subjects = ", ".join(sorted(student["subjects"]))

        print(
            f"Student ID: {student_id} | "
            f"Name: {student['name']} | "
            f"Age: {student['age']} | "
            f"Grade: {student['grade']} | "
            f"DOB: {dob} | "
            f"Subjects: {subjects}"
        )


# --------------------------------------------
# Function to Update Student Information
# --------------------------------------------
def update_student():
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


# --------------------------------------------
# Function to Delete Student
# --------------------------------------------
def delete_student():
    print("\n--- Delete Student ---")

    student_id = int(input("Enter Student ID to delete: "))

    for i in range(len(students)):

        if students[i]["personal_info"][0] == student_id:

            # del keyword is used to delete the record
            del students[i]

            print("Student deleted successfully.")

            return

    print("Student ID not found.")


# --------------------------------------------
# Function to Display Unique Subjects
# --------------------------------------------
def display_subjects():
    print("\n--- Subjects Offered ---")

    all_subjects = set()

    for student in students:

        all_subjects.update(student["subjects"])

    if len(all_subjects) == 0:

        print("No subjects found.")

        return

    print("Unique Subjects:")

    for subject in sorted(all_subjects):

        print("-", subject)


# --------------------------------------------
# Main Program
# --------------------------------------------
def main():

    print("=" * 55)
    print("       Welcome to the Student Data Organizer")
    print("=" * 55)

    while True:

        print("\nSelect an option:")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Update Student Information")
        print("4. Delete Student")
        print("5. Display Subjects Offered")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            add_student()

        elif choice == "2":

            display_students()

        elif choice == "3":

            update_student()

        elif choice == "4":

            delete_student()

        elif choice == "5":

            display_subjects()

        elif choice == "6":

            print("\nThank you for using the Student Data Organizer!")
            print("Program exited successfully.")

            break

        else:

            print("Invalid choice. Please try again.")


# Start the program
main()
