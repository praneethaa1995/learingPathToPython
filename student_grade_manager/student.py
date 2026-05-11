# Defines a Student with a name and list of grades
class Student:

    # Constructor: runs when you do Student("Alice", [90, 85])
    # self = the instance being created, name = student's name, grades = list of numbers
    def __init__(self, name, grades):
        self.name = name      # stores name on the instance
        self.grades = grades  # stores grades list on the instance

    # Calculates and returns the average of all grades
    def average(self):
        # sum(self.grades) adds all grades, divided by count
        # "if self.grades" guards against division by zero when list is empty
        return sum(self.grades) / len(self.grades) if self.grades else 0

    # Controls how the object looks when printed or converted to string
    def __str__(self):
        # f-string formats: "Alice:[90, 85] | Avg: 87.50"
        # :.2f formats the average to 2 decimal places
        return f"{self.name}:{self.grades} | Avg: {self.average():.2f}"
