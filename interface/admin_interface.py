


from db import models


def register_interface(name,password):
    admin = models.Admin.get_by_name(name)
    if not admin:
        models.Admin(name,password)
        return True,'注册成功!'
    else:
        return False,'用户已存在!'


def create_school_interface(admin_name,school_name,address):
    school = models.School.get_by_name(school_name)
    if not school:
        admin = models.Admin.get_by_name(admin_name)
        admin.create_school(school_name,address)
        return True,'创建学校成功!'
    else:
        return False,'学校已存在!'


def create_course_interface(admin_name,school_name,course_name):
    course = models.Course.get_by_name(course_name)
    if not course:
        admin = models.Admin.get_by_name(admin_name)
        admin.create_course(course_name)

        school = models.School.get_by_name(school_name)
        school.add_course(course_name)
        return True,'创建课程成功!'
    else:
        return False,'课程已存在!'


def create_teacher_interface(admin_name,teacher_name,password='123'):
    teacher = models.Teacher.get_by_name(teacher_name)
    if not teacher:
        admin = models.Admin.get_by_name(admin_name)
        admin.create_teacher(teacher_name,password)
        return True,'创建老师成功!'
    else:
        return False,'老师已存在！'




