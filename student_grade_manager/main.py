# Import necessary functions and classes from other modules
from file_handler import save_students,load_students
from utils import get_letter_grade
from student import Student


def show_menu():
    """Display the main menu options to the user"""
    print("\n1. Add Student")
    print("2. View All Students")
    print("3. Update Grades")
    print("4. Delete Student")
    print("5. View Student Report")
    print("6. Exit")

def add_student(students):
    """Add a new student with their grades to the list"""
    # Get student name from user
    name = input("enter student name")
    # Get grades as comma-separated values and convert to list of floats
    grades = list(map(float,input("enter grades").split(',')))
    # Create new Student object and add to list
    students.append(Student(name,grades))
    # Save updated list to file
    save_students(students)
    print("student added")

def view_all(students):
    """Display all students with their grades and letter grades"""
    if not students:
        print("No students found.")
    else:
        # Loop through each student and display their info
        for s in students:
            print(f"{s} | grade: {get_letter_grade(s.average())}")

def update_grades(students):
    """Update grades for an existing student"""
    # Get student name to update
    name =input("enter your name")
    # Search for student in list
    for s in students:
        if s.name ==name:
            # Get new grades and update student record
            grades = list(map(float, input("enter new grades").split(', ')))
            s.grades = grades
            # Save changes to file
            save_students(students)
            print("grades updated")
            return
    # If student not found
    print("student not found")

def delete_student(students):
    """Remove a student from the list"""
    # Get student name to delete
    name = input("enter student name to delete")
    # Search for student in list
    for s in students:
        if s.name == name:
           # Remove student from list
           students.remove(s)
           # Save changes to file
           save_students(students)
           print("student deleted")
           return
    # If student not found
    print("student not found")

def view_report(students):
    """Display detailed report for a specific student"""
    # Get student name to view
    name = input("Enter student name: ")
    # Search for student in list
    for s in students:
        if s.name == name:
            # Display full student report
            print(f"Name: {s.name}")
            print(f"Grades: {s.grades}")
            print(f"Average: {s.average():.2f}")
            print(f"Letter Grade: {get_letter_grade(s.average())}")
            return
    # If student not found
    print("Student not found.")

def main():
    """Main program loop - handles user interaction"""
    # Load existing students from file
    students = load_students()
    # Keep running until user chooses to exit
    while True:
        # Display menu options
        show_menu()
        # Get user's choice
        choice = input("Enter choice: ")
        # Execute corresponding function based on choice
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_all(students)
        elif choice == "3":
            update_grades(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            view_report(students)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

# Run main() only if this script is executed directly (not imported)
if __name__ == "__main__":
    main()
