class ClassRoom():
    def __init__(std,grade = 0,homeRoomTeacher = "",studentList=[],numStudents=0):
        std.grade = grade
        std.homeRoomTeacher = homeRoomTeacher
        std.studentList = studentList
        std.numStudents = numStudents

    def get_student_no(std,n):
        std.n = n
        return std.n

    def add_student(std,student_name):
        if len(std.studentList) >= 10:
            return False

        std.studentList.append(student_name)
        std.numStudents += 1
        return True

    def change_student(std,n, new_name):
        if n <= std.numStudents and n >= 1:
            std.studentList[n-1] = new_name
            return True
        else:  
            return False

    def remove_student(std,student_name):
        subclass = []
        for i in std.studentList:
            if i != student_name:
                subclass.append(i)
            else:
                continue
        if std.studentList == subclass:
            return False
        elif std.studentList != subclass:
            std.studentList = subclass
            std.numStudents += -1
            return True

    def remove_student_no(std,n):
        if n <= std.numStudents and n >= 1:
            del std.studentList[n-1]
            std.numStudents += -1
            return True
        else:   return False

    def set_grade(std,grade):
        std.grade = grade
    def set_homeroom_teacher(std,homeRoomTeacher):
        std.homeRoomTeacher = homeRoomTeacher
    def set_student_list(std,studentList):
        std.studentList = studentList
    def set_num_student(std,numStudents):
        std.numStudents = numStudents
    def get_grade(std):
        return std.grade
    def get_homeroom_teacher(std):
        return std.homeRoomTeacher 
    def get_student_list(std):
        return std.studentList
    def get_num_student(std):
        return std.numStudents
    def get_student_no(std,n):
        return std.studentList[n - 1]

    def __str__(std):
        nameinclass = f"Grade: {std.get_grade()}\nHomeroom Teacher: {std.get_homeroom_teacher()}\nStudents: {', '.join(std.studentList)}"
        return nameinclass


#Test section
room1 = ClassRoom()
grade = int(input("Input grade: "))
homeRoomTeacher = input("Homeroom Teacher: ")
room1.set_grade(grade)
room1.set_homeroom_teacher(homeRoomTeacher)
print(room1)

noStudent = int(input("Number of students: "))
studentList = room1.get_student_list()
room1.set_student_list(studentList)
print(room1)

for i in range(noStudent):
    temp = input(f"Student No{i+1}: ")
    if not room1.add_student(temp):
        print("Exceed 10 students.")
print(room1)
print("Grade", room1.get_grade())
print("Homeroom Teacher", room1.get_homeroom_teacher())
for i in range(room1.get_num_student()):
    print(f"No.{i+1}: {room1.get_student_no(i+1)}")

# test change_student
print(">>>>>> Testing change student")
if room1.change_student(room1.get_num_student(), "Abby"):
    print(room1)
if not room1.change_student(room1.get_num_student() + 2, "Abby"):
    print(f"Cannot change {room1.get_num_student()+2}th student")
if not room1.change_student(13, "Abby"):
    print("Index out of bound. Cannot change 13th student.")
if not room1.change_student(-1, "Abby"):
    print("Index out of bound. Cannot change -1th student.")

# test remove_student(name)
print(">>>>>> Testing remove student (name)")
if room1.get_num_student() >= 1:
    room1.remove_student(room1.get_student_no(1))
    print(room1)
if room1.get_num_student() >= 1:
    room1.remove_student(room1.get_student_no(room1.get_num_student()))
    print(room1)
if room1.get_num_student() >= 3:
    room1.remove_student(room1.get_student_no(2))
    print(room1)

# test remove_student(int)
print(">>>>>> Testing remove student no.")
room1.add_student("Bob")
room1.add_student("Mary")
room1.add_student("Adam")
if room1.get_num_student() >= 1:
    if room1.remove_student_no(1):
        print(room1)
    if not room1.remove_student_no(8):
        print(f"8 is invalid student number. There are only {room1.get_num_student()} students.")
if room1.get_num_student() >= 1:
    room1.remove_student_no(room1.get_num_student())
    print(room1)
if room1.get_num_student() >= 3:
    room1.remove_student_no(2)
    print(room1)
if room1.get_num_student() >= 3:
    room1.remove_student_no(2)
    print(room1)
if not room1.remove_student_no(-2):
    print("Index out of bound. Cannot remove -2th student.")
if not room1.remove_student_no(12):
    print("Index out of bound. Cannot remove 12th student.")