

from db import models


def register_interface(name,password):
    student = models.Student.get_by_name(name)
    if not student:
        models.Student(name,password)
        return True,'注册成功!'
    else:
        return False,'用户名已存在!'


def choice_school_interface(student_name,school_name):
    student = models.Student.get_by_name(student_name)
    if not student.school:
        student.add_school(school_name)
        return True,'选择学校成功!'
    else:
        return False,'已选择学校!'


def get_student_school_course(student_name):
    student = models.Student.get_by_name(student_name)
    if student.school:
        school = models.School.get_by_name(student.school)
        return school.course_list
    else:
        return False,'没有选择学校!'

def choice_course_interface(student_name,course_name):
    student = models.Student.get_by_name(student_name)
    student.add_course(course_name)

    course = models.Course.get_by_name(course_name)
    course.add_student(student_name)
    return True,'选择课程成功!'


def check_score(student_name):
    student = models.Student.get_by_name(student_name)
    return student.scores
