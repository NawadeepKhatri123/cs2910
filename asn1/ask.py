import csv

#students function
def students():
    enter = input ("(L)List Students (S)Search Students (E)Exit to Main Menu : ")

    if enter.lower() == "l":
        enter = input("(L)Unorderd List (S)Sorted List (R)Reverse Sorted List : ")
        
        if enter.lower() == "l":
             get_students(L = True)
        elif enter.lower() == "s":
            get_students(S = True)
        elif enter.lower() == "r":
            get_students(R = True)
    
    elif enter.lower() == "s":
        enter = input("Search : (L)Last Name (P)Phone Number : ")
        
        if enter.lower() == "l":
            enter = input("Enter last name : ")
            get_students(LN = enter)
        elif enter.lower() == "p":
            enter = input("Enter phone number : ")
            get_students(P = enter)

def get_students(L = None, S = None, R = None, LN = None , P = None):

    
    with open ("students.csv","r") as file:
        # read file
        reader = csv.reader(file,delimiter=";")
        # list for names
        names = []

        for row in reader:

            #outputs list of all students
            if L is not None:
                print(row)
            #add to list
            elif S is not None:
                names.append(row[2] + row[1])
            elif R is not None:
                names.append(row[2] + row[1])
            #outputs the info of student with matching last name
            elif LN is not None:
                if LN.lower() == row[1].lower():
                    print(row)
            #outputs for info of students with matching phone numbers
            elif P is not None:
                if P == row[3]:
                    print(row)

        if S is not None:
            names.sort()
            print(names)
        if R is not None:
            names.sort(reverse = True)
            print(names)


# courses function
def courses():

    enter = input("(A)Add New Courses (O)Output Courses (E) Exit to Main Menu : ")
    if enter.lower() == "a":
        courses_Input("hello")
    elif enter.lower() == "e":
        main()
    elif enter.lower() == "o": 
        enter = input("(L)List Courses (E)Enter Semester (S)Search by name/code : ")
            #input for list
        if enter.lower() == "l":
            enter = input("List Courses: (U)Unsorted (S)Sorted (R)Reverse Sorted : ")
            if enter.lower() == "u":
                courses_Output(U = True)
            elif enter.lower() == "s":
                courses_Output(S = True)
            elif enter.lower() == "r":
                courses_Output(R = True)
        # input for semester
        elif enter.lower() == "e":
            enter = input ("(W)Winter (F)Fall : ")
            if enter.lower() == "w":
                courses_Output(W = True)
            elif enter.lower() == "f":
                courses_Output(F = True)
        # input for search 
        elif enter.lower() == "s":    
            enter = input("Search Courses: (N)Name (C)Code : ")
            if enter.lower() == "n":
                enter = input("Enter the course Name : ")
                courses_Output(N = enter)
            if enter.lower() == "c":
                enter = input("Enter the course code : ")
                courses_Output(C = enter)

def courses_Input(c_course):
    pass
# prints courses if selects output
def courses_Output(U = None , S = None ,R = None ,N = None ,C = None ,W = None ,F = None ): 
    lists = []
    list_sem = []
    with open ("courses.csv","r") as file:
        reader = csv.reader(file,delimiter = ";") 
            

        for i in reader:

            # prints the Unsorted list
            if U is not None:
                print(i[0])
            # adds to the list for sorted or reverse sorted
            elif S is not None or R is not None:
                lists.append(i[0])
            # adds to the Winter list
            elif W is not None:
                if i[1] == "winter":
                    list_sem.append(i[0])
            # adds to the fall list
            elif F is not None:
                if i[1] == "fall":
                    list_sem.append(i[0])
            # adds to the name list
            elif N is not None:
                if i[0].lower() == N.lower():
                    print(i)
            #prints course by code
            elif C is not None:
                if i[0].lower() == C.lower():
                    print(i)

        #prints out the sorted list
        if S is not None:
            lists.sort()
            for i in lists:
                print(i)
        #prints out the reverse sorted list
        elif R is not None:
            lists.sort(reverse = True)
            for i in lists:
                print(i)
        #prints out the Winter semester courses
        elif W is not None:
            list_sem.sort()
            for i in list_sem:
                print(i)
        #prints out the Fall semester courses
        elif F is not None:
            list_sem.sort()
            for i in list_sem:
                print(i)
        
            

            


# grades function
def grades():
   pass 
def main():

    choice = input("(S) Students (C) Courses (G) Grades (E) Exit : ")
    students()
#entry point
if __name__ == "__main__":
    main()
