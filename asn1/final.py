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

    def print_list(self,students,a,b):
        if a != True and b != True:
            for i in students:
                print()
                print(i)
        elif a == True:
            students.sort(key = lambda student : student.first_name)
            for i in students:
                print()
                print(i)
        else:
            students.sort(key = lambda student : student.first_name, reverse = True)
            for i in students:
                print()
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
                print()
                print(course)
            elif self.course_id == course.course_id:
                print()
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
            writer.writerow([student.id, student.last_name, student.first_name, student.ph, student.email])
def add_student_info(student):
    with open('students.csv', mode='a', newline='') as file:  # Use 'a' mode to append
        writer = csv.writer(file, delimiter=';')
        writer.writerow([student.id, student.last_name, student.first_name, student.ph, student.email])


def update_Cinfo(courses):
    with open('courses.csv',mode = 'a', newline='')as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerow([courses.course_name, courses.semester,courses.course_id])

def add_grade_info(student):
     with open('grades.csv', mode='a', newline='') as file:  # Use 'a' mode to append
         writer = csv.writer(file, delimiter=';')
         writer.writerow([student.id, student.last_name, student.first_name, student.c1,student.c2,student.c3,student.c4])

def main():
    while(True):

        students = []
        with open('students.csv', mode='r') as file:
            reader = csv.reader(file, delimiter=';')

            for row in reader:
                student_id = int(row[0])
                last_name = row[1]
                first_name = row[2]
                ph = row[3]
                email = row[4]

                # create a instance of the student class
                student = Students(student_id, last_name, first_name, ph, email)

                students.append(student)

        courses = []
        with open('courses.csv', mode='r') as file:
            reader = csv.reader(file, delimiter=';')

            for row in reader:
                course_name = row[0]
                semester = row[1]
                course_id = row[2]

                course = Courses(course_name, semester, course_id)
                courses.append(course)
        grades = []
        with open('grades.csv', mode='r') as file:
            reader = csv.reader(file, delimiter=";")

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

                grade = Grades(student_id, last_name, first_name, c1, c2, c3, c4)
                grades.append(grade)





        print()
        enter = input ( "\033[31mView : (S)Student info (C)Courses Info (G)Grades (A)Add (E)Exit : \033[0m")
        if enter.lower() == 's':
            print()
            enter = input ("\033[31mStudent : (U)Update (L)List (S)Search (E)Exit to Main Menu : \033[0m")
            if enter.lower() == 'l':
                print()
                enter = input("\033[31mList : (U)Unordered (O)Ordered (R)Reversed (E)Exit to Main Menu : \033[0m")
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
                enter_id = int(input("\033[33mEnter student id: \033[0m"))
                student_found = False

                for student in students:
                    if student.id == enter_id:

                        print()
                        print(student)
                        print()
                        enter = input("\033[31mUpdate: (L)Last Name (F)First Name (P)Phone Number (E)Email: \033[0m")

                        if enter.lower() == 'l':
                            enter = input("\033[33mEnter new last name: \033[0m")
                            student.last_name = enter
                        elif enter.lower() == 'f':
                            enter = input("\033[33mEnter new first name: \033[0m")
                            student.first_name = enter
                        elif enter.lower() == 'p':
                            enter = input("\033[33mEnter new phone number: \033[0m")
                            student.ph = enter
                        elif enter.lower() == 'e':
                            enter = input("\033[33mEnter new email address: \033[0m")
                            student.email = enter
                        update_Sinfo(students)
                        continue
            elif enter.lower() == 's':
                print()
                enter = input ("\033[31mSearch : (L)Last Name (P)Phone number (E) Exit to Main Menu : \033[0m")
                if enter.lower() == 'l':
                    #search for student from lastname
                    enter = input("\033[33mEnter last name : \033[0m")
                    enter = enter.upper();
                    SN_name = Students(None, enter, None,None,None)
                    SN_name.search(students)
                elif enter.lower() == 'p':
                    #search for student from phone number
                    enter = input("\033[33menter phone number : \033[0m")
                    SN_ph = Students(None, None,None,enter,None)
                    SN_ph.search(students)

                elif enter.lower() == 'e':
                    pass
                continue

        elif enter.lower() == 'c':
            print()
            enter = input ("\033[31mCourse : (L)List (S)Search (E)Exit to Main Menu : \033[0m")
            if enter.lower() == 'l':
                print()
                enter = input("\033[31mList : (U)Unordered (O)Ordered (R)Reversed (E)Exit to Main Menu : \033[0m")
                if enter.lower() == 'u':
                    Stu_order = Courses(None,None,None)
                    Stu_order.print_list(courses,False,False)
                elif enter.lower() == 'o':
                    Stu_order = Courses(None,None,None)
                    Stu_order.print_list(courses,True,False)
                elif enter.lower() == 'r':
                    Stu_order = Courses(None,None,None)
                    Stu_order.print_list(courses,False,True)
                elif enter.lower() == 'e':
                    pass
                continue
            elif enter.lower() == 's':
                print()
                enter = input ("\033[31mSearch : (N)Name (C)Code (S)Semester (E) Exit to Main Menu : \033[0m")
                if enter.lower() == 'n':
                    #search for course name
                    print()
                    enter = input("\033[33mEnter course name : \033[0m")
                    enter = enter.upper()
                    S_name = Courses(enter, None, None)
                    S_name.search(courses)
                elif enter.lower() == 'c':
                    # search for course code
                    print()
                    enter = input("\033[33mEnter course code : \033[0m")
                    S_id = Courses(None, None, enter)
                    S_id.search(courses)
                elif enter.lower() == 's':
                    # output for semester
                    print()
                    enter = input("\033[33mEnter semester : \033[0m")
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
            gg_grade1 = []
            l_name, c_code = input ("\033[33mEnter last name and course code : \033[0m").split()
            for course in courses:
                enter = input(f"\033[33mEnter grades for {course.course_name} : \033[0m")
                if not enter:
                    gg_grade1.append('na')
                else:
                    gg_grade1.append(enter)
            new_student = Students(99, l_name, 'xyz', 1234, '@@@')
            new_course = Courses(c_code, 'fall', 1234)
            new_grade = Grades(99,l_name,'xyz',gg_grade1[0],gg_grade1[1],gg_grade1[2],gg_grade1[3])
            add_student_info(new_student)
            update_Cinfo(new_course)
            add_grade_info(new_grade)
            continue
        elif enter.lower() == 'g':

            #map students grades courses
            cg_list = []
            new_list = []
            new_list1 =[]
            for i in courses:
                cg_list.append(i.course_name)
            print()
            enter = input("\033[31mGrades : (O)Stu Course & Grades (C)Stu Avg (CA)C+Term (AC)Avg Course Grades : \033[0m")
            #output list of all courses taken by a student

            if enter.lower() == 'o':
                print()
                enter = input("\033[32mEnter last name : \033[0m")
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
                    print(f"\033[33m{grade.first_name},{grade.last_name}, {new_list}\033[0m")
                    avg = 0
                    new_list.clear()

                ##########################################################
            elif enter.lower() == 'c':#average
                print()
                enter = input("\033[32mEnter last name : \033[0m")
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
                    if len(new_list) != 0:
                        print(f"\033[34m{grade.first_name},{grade.last_name} average = {avg/len(new_list)}\033[0m")
                    avg = 0
                    new_list.clear()

            elif enter.lower() == 'ca':
                list_ca=[]
                avg = 0

                semester1 = ['winter','fall','spring']
                print()
                enter = input("\033[33mEnter student's last Name : \033[0m")
                enter_1 = input("\033[33mEnter course term : \033[0m")

                for grade in grades:
                    if grade.last_name.lower() == enter.lower():
                        list_ca.append(grade)


                count = 0
                for i in list_ca:
                    count = 0
                    avg = 0
                    if enter_1 == 'winter':
                        if i.c1 != 'na':
                            avg = avg + i.c1
                            count += 1
                        if i.c4 != 'na':
                            avg = avg + i.c4
                            count += 1
                    elif enter_1 == 'fall':
                        if i.c2 != 'na':
                            avg = avg + i.c2
                            count += 1
                        if i.c3 != 'na':
                            avg = avg + i.c4
                            count +=1
                    if count != 0:
                        print()
                        print(f"\033[34m{i.first_name},{i.last_name} {enter_1} average = {avg / count}\033[0m")

                pass
            elif enter.lower() == 'ac':
                print()
                enter = input("\033[33mEnter the course name : \033[0m")
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
                    print("\033[34mno grades found")
                else:

                    print(f"\033[34mthe average grade for {enter} is {avg/count1}\033[0m")

        elif enter.lower() == 'e':
            sys.exit(0)
        else:
            print()
            print("\033[34mInvalid input\033[0m")
            continue

if __name__ == "__main__":
    main()




