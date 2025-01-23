import csv
import sys
class Students:
    def __init__(self, student_id, last_name, first_name, ph,email):
        self.id = student_id
        self.last_name = last_name
        self.first_name = first_name
        self.ph = ph
        self.email = email

    def search(self, students):
        for student in students:
            if self.last_name == student.last_name.upper():
                print(student)
            elif self.ph == student.ph:
                print(student)

    def print_list(self,courses,a,b):
        if a != True and b != True:
            for i in courses:
                print(i)
        elif a == True:
            courses.sort(key = lambda course : course.last_name)
            for i in courses:
                print(i)
        else:
            courses.sort(key = lambda course : course.last_name, reverse = True)
            for i in courses:
                print(i)
    def __str__(self):
        return f"{self.id},{self.last_name}, {self.first_name}, {self.ph},{self.email}"


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

    def print_list(self,courses,a,b):
        if a != True and b != True:
            for i in courses:
                print(i)
        elif a == True:
            courses.sort(key = lambda course : course.course_name)
            for i in courses:
                print(i)
        else:
            courses.sort(key = lambda course : course.course_name, reverse = True)
            for i in courses:
                print(i)

class Grades:
    def __init__(self, student_id,last_name,first_name, c1, c2, c3, c4):
        self.id = student_id
        self.last_name = last_name
        self.first_name = first_name
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4

def update_Sinfo(students):
    with open('students.csv',mode = 'w', newline='')as file:
        writer = csv.writer(file, delimiter = ';')
        for student in students:
            writer.writerow([student.id, student.first_name, student.last_name, student.ph, student.email])
def add_student_info(student):
    with open('students.csv', mode='a', newline='') as file:  # Use 'a' mode to append
        writer = csv.writer(file, delimiter=';')
        writer.writerow([student.id, student.first_name, student.last_name, student.ph, student.email])


def update_Cinfo(courses):
    with open('courses.csv',mode = 'a', newline='')as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerow([courses.course_name, courses.semester,courses.course_id])

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

  
    courses = []
    with open('courses.csv', mode = 'r') as file:
        reader = csv.reader(file, delimiter = ';')

        for row in reader:
            course_name = row[0]
            semester = row[1]
            course_id = row[2]

            course = Courses(course_name, semester, course_id)
            courses.append(course)
    grades = []
    with open('grades.csv', mode = 'r') as file:
        reader = csv.reader(file,delimiter = ";")

        for row in reader:
            student_id = int(row[0])
            last_name = row[1]
            first_name = row[2]
            if row[3] != 'na':
                c1 = int(row[3])
            else:
                c1 = row[3]
            if row[4] != 'na':
                c2 = int(row[4])
            else:
                c2 = row[4]
            if row[5] != 'na':
                c3 = int(row[5])
            else:
                c3 = row[5]
            if row[6] != 'na':
                c4 = int(row[6])
            else:
                c4 = row[6]


            grade = Grades(student_id,last_name,first_name, c1,c2,c3,c4)
            grades.append(grade)

    while(True):
        print()
        enter = input ( "View : (S)Student info (C)Courses Info (G)Grades (A)Add (E)Exit : ")
        if enter.lower() == 's':
            print()
            enter = input ("Student : (U)Update (L)List (S)Search (E)Exit to Main Menu : ")
            if enter.lower() == 'l':
                print()
                enter = input("List : (U)Unordered (O)Ordered (R)Reversed (E)Exit to Main Menu : ")
                if enter.lower() == 'u':
                    Stu_order = Students(None,None,None,None,None)
                    Stu_order.print_list(students,False,False)
                elif enter.lower() == 'o':
                    Stu_order = Students(None,None,None,None,None)
                    Stu_order.print_list(students,True,False)
                elif enter.lower() == 'r':
                    Stu_order = Students(None,None,None,None,None)
                    Stu_order.print_list(students,False,True)
                elif enter.lower() == 'e':
                    pass
                continue
            elif enter.lower() == 'u':
                enter_id = int(input("Enter student id: "))
                student_found = False

                for student in students:
                    if student.id == enter_id:

                        print()
                        print(student)
                        print()
                        enter = input("Update: (L)Last Name (F)First Name (P)Phone Number (E)Email: ")

                        if enter.lower() == 'l':
                            enter = input("Enter new last name: ")
                            student.last_name = enter
                        elif enter.lower() == 'f':
                            enter = input("Enter new first name: ")
                            student.first_name = enter
                        elif enter.lower() == 'p':
                            enter = input("Enter new phone number: ")
                            student.ph = enter
                        elif enter.lower() == 'e':
                            enter = input("Enter new email address: ")
                            student.email = enter
                        update_Sinfo(students)
                        continue
            elif enter.lower() == 's':
                print()
                enter = input ("Search : (L)Last Name (P)Phone number (E) Exit to Main Menu : ")
                if enter.lower() == 'l':
                    #search for student from lastname
                    enter = input("Enter last name : ")
                    enter = enter.upper();
                    SN_name = Students(None, enter, None,None,None)
                    SN_name.search(students)
                elif enter.lower() == 'p':
                    #search for student from phone number
                    enter = input("enter phone number : ")
                    SN_ph = Students(None, None,None,enter,None)
                    SN_ph.search(students)

                elif enter.lower() == 'e':
                    pass
                continue

        elif enter.lower() == 'c':
            print()
            enter = input ("Course : (L)List (S)Search (E)Exit to Main Menu : ")
            if enter.lower() == 'l':
                print()
                enter = input("List : (U)Unordered (O)Ordered (R)Reversed (E)Exit to Main Menu : ")
                if enter.lower() == 'u':
                    Stu_order = Courses(None,None,None)
                    Stu_order.print_list(courses,False,False)
                elif enter.lower() == 'o':
                    Stu_order = Students(None,None,None)
                    Stu_order.print_list(courses,True,False)
                elif enter.lower() == 'r':
                    Stu_order = Students(None,None,None)
                    Stu_order.print_list(courses,False,True)
                elif enter.lower() == 'e':
                    pass
                break
            elif enter.lower() == 's':
                print()
                enter = input ("Search : (N)Name (C)Code (S)Semester (E) Exit to Main Menu : ")
                if enter.lower() == 'n':
                    #search for course name
                    print()
                    enter = input("Enter course name : ")
                    enter = enter.upper()
                    S_name = Courses(enter, None, None)
                    S_name.search(courses)
                elif enter.lower() == 'p':
                    # search for course code
                    print()
                    enter = input("Enter course code : ")
                    S_id = Courses(None, None, enter)
                    S_id.search(courses)
                elif enter.lower() == 's':
                    # output for semester
                    print()
                    enter = input("Enter semester : ")
                    new_list = []
                    # add to new list
                    for i in courses:
                        if i.semester == enter.lower():
                            new_list.append(i)
                    S_sem = Courses(None, None, None)
                    S_sem.print_list(new_list,True,False)
                elif enter.lower() == 'e':
                    pass
                continue
        elif enter.lower() == 'a':
            print()
            l_name, c_code = input ("Enter last name and course code : ").split()
            new_student = Students(99, l_name, 'xyz', 1234, '@@@')
            new_course = Courses(c_code, 'fall', 1234)
            add_student_info(new_student)
            update_Cinfo(new_course)
            continue
        elif enter.lower() == 'g':

            #map students grades courses
            cg_list = []
            new_list = []
            new_list1 =[]
            for i in courses:
                cg_list.append(i.course_name)
            print()
            enter = input("Grades : (O)Stu Course & Grades (C)Stu Avg (CA)C+Term (AC)Avg Course Grades : ")
            #output list of all courses taken by a student

            if enter.lower() == 'o':
                print()
                enter = input("Enter last name : ")
                avg = 0
                for grade in grades:
                    if grade.last_name.lower() == enter.lower():
                        if grade.c1 != 'na':
                            new_list.append((cg_list[0], grade.c1))
                        if grade.c2 != 'na':
                            new_list.append((cg_list[1], grade.c2))
                        if grade.c3 != 'na':
                            new_list.append((cg_list[2], grade.c3))
                        if grade.c4 != 'na':
                            new_list.append((cg_list[3], grade.c4))
                    print(f"{grade.first_name},{grade.last_name}, {new_list}")
                    avg = 0
                    new_list.clear()

                ##########################################################
            elif enter.lower() == 'c':#average
                print()
                enter = input("Enter last name : ")
                avg = 0
                for grade in grades:
                    if grade.last_name.lower() == enter.lower():
                        if grade.c1 != 'na':
                            new_list.append(0)
                            avg += grade.c1
                        if grade.c2 != 'na':
                            new_list.append(0)
                            avg += grade.c2
                        if grade.c3 != 'na':
                            new_list.append(0)
                            avg += grade.c3
                        if grade.c4 != 'na':
                            new_list.append(0)
                            avg += grade.c4

                    print(f"{grade.first_name},{grade.last_name} average = {avg/len(new_list)}")
                    avg = 0
                    new_list.clear()

            elif enter.lower() == 'ca':
                pass
            elif enter.lower() == 'ac':
                print()
                enter = input("Enter the course name : ")
                list_course = []
                list_fall = []
                avg = 0
                count1 = 0
                count = 1
                for i in cg_list:
                    if i.lower() == enter.lower():
                        list_course.append(count)

                    else:
                        list_course.append(0)
                for grade in grades:
                    if grade.c1 != 'na' and list_course[0] == 1:
                        list_fall.append(grade.c1)
                        count1 = count1 + 1
                    if grade.c2 != 'na' and list_course[1] == 1:
                        list_fall.append(grade.c2)
                        count1 = count1 + 1
                    if grade.c3 != 'na' and list_course[2] == 1:
                        list_fall.append(grade.c3)
                        count1 = count1 + 1
                    if grade.c1 != 'na' and list_course[3] == 1:
                        list_fall.append(grade.c4)
                        count1 = count1 + 1
                for i in list_fall:
                    avg = avg + i
                print()
                if count1 == 0:
                    print("no grades found")
                else:

                    print(f"the average grade for {enter} is {avg/count1}")

        elif enter.lower() == 'e':
            sys.exit(0)
        else:
            print()
            print("Invalid input")
            continue









if __name__ == "__main__":
    main()




