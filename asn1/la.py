import csv

class Person:
    def __init__(self, id, last_name, first_name, ph, email):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.ph = ph
        self.email = email

    def __str__(self):
        return f"{self.id},{self.last_name},{self.first_name},{self.ph},{self.email}"

    @classmethod
    def search(cls, objects, key, value):
        return [obj for obj in objects if getattr(obj, key).upper() == value.upper()]

class Students(Person):
    pass

class Courses:
    def __init__(self, course_name, semester, course_id):
        self.course_name = course_name
        self.semester = semester
        self.course_id = course_id

    def __str__(self):
        return f"{self.course_id},{self.course_name},{self.semester}"

    @classmethod
    def search(cls, objects, key, value):
        return [obj for obj in objects if getattr(obj, key).upper() == value.upper()]

def load_csv(file_path, class_type, delimiter=';'):
    objects = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file, delimiter=delimiter)
        for row in reader:
            obj = class_type(*row)
            objects.append(obj)
    return objects

def list_objects(objects, order=False, reverse=False):
    sorted_objects = sorted(objects, key=lambda x: x.first_name if isinstance(x, Students) else x.course_name, reverse=reverse)
    for obj in sorted_objects:
        print(obj)

def main():
    students = load_csv('students.csv', Students)
    courses = load_csv('courses.csv', Courses)

    while True:
        action = input("View: (S) Student info (C) Courses info (G) Grades (E) Exit: ").lower()
        if action == 's':
            student_action = input("Student: (L) List (S) Search (E) Exit to Main Menu: ").lower()
            if student_action == 'l':
                list_action = input("List: (U) Unordered (O) Ordered (R) Reversed (E) Exit to Main Menu: ").lower()
                if list_action == 'u':
                    list_objects(students)
                elif list_action == 'o':
                    list_objects(students, order=True)
                elif list_action == 'r':
                    list_objects(students, reverse=True)
            elif student_action == 's':
                search_action = input("Search: (L) Last Name (P) Phone number (E) Exit to Main Menu: ").lower()
                if search_action == 'l':
                    last_name = input("Enter last name: ").upper()
                    results = Students.search(students, 'last_name', last_name)
                    for result in results:
                        print(result)
                elif search_action == 'p':
                    phone = input("Enter phone number: ")
                    results = Students.search(students, 'ph', phone)
                    for result in results:
                        print(result)
        elif action == 'c':
            course_action = input("Course: (L) List (S) Search (E) Exit to Main Menu: ").lower()
            if course_action == 'l':
                list_action = input("List: (U) Unordered (O) Ordered (R) Reversed (E) Exit to Main Menu: ").lower()
                if list_action == 'u':
                    list_objects(courses)
                elif list_action == 'o':
                    list_objects(courses, order=True)
                elif list_action == 'r':
                    list_objects(courses, reverse=True)
            elif course_action == 's':
                search_action = input("Search: (N) Name (C) Code (S) Semester (E) Exit to Main Menu: ").lower()
                if search_action == 'n':
                    course_name = input("Enter course name: ").upper()
                    results = Courses.search(courses, 'course_name', course_name)
                    for result in results:
                        print(result)
                elif search_action == 'c':
                    course_code = input("Enter course code: ")
                    results = Courses.search(courses, 'course_id', course_code)
                    for result in results:
                        print(result)
                elif search_action == 's':
                    semester = input("Enter semester: ").lower()
                    results = [course for course in courses if course.semester == semester]
                    list_objects(results, order=True)
        elif action == 'e':
            break

if __name__ == "__main__":
    main()

