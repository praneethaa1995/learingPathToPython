# Student Grade Manager

A command-line Python application to manage student records and grades with persistent file storage.

## Project Structure

```
student_grade_manager/
├── data/
│   └── student.txt       # Persistent storage for student records
├── student.py            # Student class / data model
├── file_handler.py       # Read/write operations on student.txt
├── utils.py              # Helper functions (GPA calc, grade logic, etc.)
├── main.py               # Entry point, CLI menu
└── README.md
```

## Features

- Add, update, and delete student records
- Assign and manage grades per subject
- Calculate averages and GPA
- Persist data to `data/student.txt`
- View all students and their grades

## How to Run

```bash
cd student_grade_manager
python main.py
```

## Requirements

- Python 3.x
- No external dependencies

## Modules Overview

| File | Responsibility |
|---|---|
| `student.py` | Defines the `Student` class with name, ID, and grades |
| `file_handler.py` | Loads and saves student data to/from `student.txt` |
| `utils.py` | Grade calculations, GPA logic, input validation |
| `main.py` | CLI menu loop, ties all modules together |

## Data Format (`student.txt`)

Each line stores one student record, e.g.:

```
101,Alice,Math:90,Science:85,English:92
102,Bob,Math:78,Science:80,English:74
```

## Example Usage

```
1. Add Student
2. View All Students
3. Update Grades
4. Delete Student
5. View Student Report
6. Exit
```
