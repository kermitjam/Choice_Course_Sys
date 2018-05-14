

from db import models
def check_courses_interface(teacher_name):
    teacher = models.Teacher.get_by_name(teacher_name)
    return teacher.course_list


def get_course_list_interface(school_name):
    school = models.School.get_by_name(school_name)
    return school.course_list


def choice_course_interface(teacher_name,course_name):
    teacher = models.Teacher.get_by_name(teacher_name)
    teacher.add_course(course_name)
    return True,'选择课程成功!'

def check_student_interface(course_name):
    course = models.Course.get_by_name(course_name)
    return course.student_list

def modify_interface(teacher_name,student_name,course_name,score):
    teacher = models.Teacher.get_by_name(teacher_name)
    teacher.modify_score(student_name,course_name,score)
    return True,'修改分数成功！'




