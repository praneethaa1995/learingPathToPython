# Import Student class from student.py to create Student objects when loading
from student import Student

# Constant for the file path — change this one line if file location changes
FILE = "data/student.txt"

def save_students(students):
    # Open file in write mode ("w"), auto-closes when done via "with"
    with open(FILE, "w") as f:
        for s in students:  # loop through each Student object
            # convert grades list [90,85] → "90,85" (numbers to strings, joined by comma)
            grades = ",".join(map(str, s.grades))
            # write one line per student e.g. "Alice:90,85\n"
            f.write(f"{s.name}:{grades}\n")

def load_students():
    students = []  # empty list to collect loaded Student objects
    try:
        # Open file in read mode ("r"), try block handles missing file
        with open(FILE, "r") as f:
            for line in f:  # read file line by line
                line = line.strip()  # remove whitespace and \n → "Alice:90,85"
                if line:  # skip blank lines
                    # split "Alice:90,85" by ":" → name="Alice", grades="90,85"
                    name, grades = line.split(":")
                    # grades.split(",") → ["90","85"]
                    # map(float, ...) → [90.0, 85.0]
                    # list(...) → proper list, Student(...) → creates Student object
                    students.append(Student(name, list(map(float, grades.split(",")))))
    except FileNotFoundError:
        pass  # file doesn't exist yet (first run), do nothing instead of crashing
    return students  # return list of Student objects (outside except — bug fix)
