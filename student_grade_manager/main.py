# TODO: import load_students and save_students from file_handler
# TODO: import get_letter_grade from utils
# TODO: import Student from student

# TODO: define show_menu() — prints the 6 menu options:
#       1. Add Student
#       2. View All Students
#       3. Update Grades
#       4. Delete Student
#       5. View Student Report
#       6. Exit

# TODO: define add_student(students) — ask for name, ask for grades (comma-separated),
#       convert input to list of floats, create Student(name, grades),
#       append to students list, call save_students(students)

# TODO: define view_all(students) — loop through students list,
#       print each student using print(s) which calls Student.__str__
#       also print the letter grade using get_letter_grade(s.average())
#       if list is empty, print "No students found."

# TODO: define update_grades(students) — ask for student name to update,
#       find the student in the list (loop and match s.name),
#       ask for new grades (comma-separated), update s.grades,
#       call save_students(students), print confirmation
#       if not found, print "Student not found."

# TODO: define delete_student(students) — ask for student name to delete,
#       find and remove the student from the list,
#       call save_students(students), print confirmation
#       if not found, print "Student not found."

# TODO: define view_report(students) — ask for student name,
#       find the student, print full report:
#         name, grades list, average (:.2f), letter grade
#       if not found, print "Student not found."

# TODO: define main() —
#       call load_students() to get the students list
#       start a while True loop:
#           call show_menu()
#           read user choice with input()
#           call the matching function based on choice (1-6)
#           if choice == "6": print "Goodbye!" and break
#           handle invalid input with else: print "Invalid choice."

# TODO: call main() using:
# if __name__ == "__main__":
#     main()
