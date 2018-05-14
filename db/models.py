

from db import db_handler
class BaseClass:

    @classmethod
    def get_by_name(cls,name):
        return db_handler.select(name,cls.__name__.lower())

    def save(self):
        db_handler.save(self)


class Admin(BaseClass):
    def __init__(self,name,password):
        self.name = name
        self.password = password
        self.save()

    def create_school(self,school,address):
        school = School(school,address)
        school.save()

    def create_course(self,course_name):
        course = Course(course_name)
        course.save()

    def create_teacher(self,teacher_name,password):
        teacher = Teacher(teacher_name,password)
        teacher.save()

class School(BaseClass):
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.course_list = []

    def add_course(self,course_name):
        self.course_list.append(course_name)
        self.save()

class Course(BaseClass):
    def __init__(self,name):
        self.name = name
        self.student_list = []


    def add_student(self,student_name):
        self.student_list.append(student_name)
        self.save()

class Teacher(BaseClass):
    def __init__(self,name,password):
        self.name = name
        self.password = password
        self.course_list = []

    def add_course(self,course_name):
        self.course_list.append(course_name)
        self.save()

    def modify_score(self,student_name,course_name,score):
        student = Student.get_by_name(student_name)
        student.scores[course_name] = score
        student.save()


class Student(BaseClass):
    def __init__(self,name,password):
        self.name = name
        self.password = password
        self.school = None
        self.course_list = []
        self.scores = {}
        self.save()

    def add_school(self,school_name):
        self.school = school_name
        self.save()

    def add_course(self,course_name):
        self.course_list.append(course_name)
        self.scores[course_name] = 0
        self.save()













