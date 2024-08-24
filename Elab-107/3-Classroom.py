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
        else: return False

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
            return True

    def remove_student_no(std,n):
        if n <= std.numStudents and n >= 1:
            del std.studentList[n-1]
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