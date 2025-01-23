import csv

class Students:
    def __init__(self, student_id, last_name, first_name, ph,email):
        self.id = student_id
        self.last_name = last_name
        self.first_name = first_name
        self.ph = ph
        self.email = email

class Courses:
    def __init__(self, course_name, semester, course_id):
        self.course_name = course_name
        self.semester = semester
        self.course_id = course_id

    def __str__(self):
        return f"{self.course_id},{self.course_name}, {self.semester}"

    def search(self, courses ):
        for course in courses:
            if self.course_name == course.course_name:
                print(course)
            elif self.course_id == course.course_id:
                print(course)

def main():
    students = []
    with open('students.csv',mode = 'r')as file:
        reader = csv.reader(file, delimiter=';')

        for row in reader:
            student_id = int(row[0])
            last_name = row[1]
            first_name = row[2]
            ph = row[3]
            email = row[4]

            # create a instance of the student class
            student = Students(student_id, last_name, first_name, ph,email)

            students.append(student)
    students.sort(key = lambda student : student.first_name)
    for student in students:
        print(student.first_name)
  
    courses = []
    with open('courses.csv', mode = 'r') as file:
        reader = csv.reader(file, delimiter = ';')

        for row in reader:
            course_name = row[0]
            semester = row[1]
            course_id = row[2]

            course = Courses(course_name, semester, course_id)
            courses.append(course)
    courses.sort(key = lambda course : course.course_name , reverse = True )
    for course in courses:
        print(course)

    #search for course name
    enter = input("enter course name : ")
    enter = enter.upper()
    S_name = Courses(enter, None, None)
    S_name.search(courses)
    # search for course code
    enter = input("enter course code : ")
    S_id = Courses(None, None, enter)
    S_id.search(courses)

if __name__ == "__main__":
    main()




