

from lib import common
from interface import teacher_interface,common_interface
teacher_info = {
    'name':None
}

def login():
    while True:
        name = input('请输入用户名:').strip()
        password = input('请输入密码:').strip()
        flag,msg = common_interface.login_interface(name,password,'teacher')
        if flag:
            print(msg)
            teacher_info['name']= name
            break
        else:
            print(msg)

@common.auth_login(type='teacher')
def check_course():
    course_list = teacher_interface.check_courses_interface(teacher_info['name'])
    for course in course_list:
        print(course)



@common.auth_login(type='teacher')
def choice_course():
    while True:
        school_list = common.check_files('school')
        for i,school in enumerate(school_list):
            print('%s   %s' %(i,school))
        choice = input('请选择学校:').strip()
        if choice.isdigit():
            choice = int(choice)
            if choice < len(school_list):
                course_list = teacher_interface.get_course_list_interface(school_list[choice])
                for i,course in enumerate(course_list):
                    print('%s   %s' %(i,course))
                choice_course = input('请选择课程:').strip()
                if choice_course.isdigit():
                    choice_course = int(choice_course)
                    if choice_course < len(course_list):
                        flag,msg = teacher_interface.choice_course_interface(teacher_info['name'],course_list[choice_course])
                        if flag:
                            print(msg)
                            break
                        else:
                            print(msg)
                    else:
                        print('必须是课程编号!')
                else:
                    print('必须是数字！')
            else:
                print('必须是学校编号！')
        else:
            print('必须是数字')





@common.auth_login(type='teacher')
def check_student():
    course_list = teacher_interface.check_courses_interface(teacher_info['name'])
    for i,course in enumerate(course_list):
        print('%s %s'%(i,course))
    choice = input('请选择课程').strip()
    if choice.isdigit():
        choice = int(choice)
        if choice<len(course_list):
            student_list = teacher_interface.check_student_interface(course_list[choice])
            for student in student_list:
                print(student)
                break
        else:
            print('必须为课程编号')
    else:
        print('必须是数字！')

@common.auth_login(type='teacher')
def modify_score():
    while True:
        course_list = teacher_interface.check_courses_interface(teacher_info['name'])
        for i,course in enumerate(course_list):
            print('%s %s' %(i,course))
        choice = input('请选择课程:').strip()
        if choice.isdigit():
            choice = int(choice)
            if choice < len(course_list):
                student_list = teacher_interface.check_student_interface(course_list[choice])
                for i,student in enumerate(student_list):
                    print('%s %s' %(i,student))
                choice_student = input('请选择学生:').strip()
                if choice_student.isdigit():
                    choice_student = int(choice_student)
                    if choice_student<len(student_list):
                        input_score = input('请输入修改分数:').strip()
                        if input_score.isdigit():
                            input_score = int(input_score)
                            flag,msg = teacher_interface.modify_interface(teacher_info['name'],student_list[choice_student],course_list[choice],input_score)
                            if flag:
                                print(msg)
                                break
                            else:
                                print(msg)
                        else:
                            print('必须是数字!')
                    else:
                        print('必须是编号!')
                else:
                    print('必须是数字！')
            else:
                print('必须是编号!')
        else:
            print('必须是数字！')



teacher_dic = {
    '1':login,
    '2':check_course,
    '3':choice_course,
    '4':check_student,
    '5':modify_score
}

def teacher_view():
    while True:
        print('''
        1 老师登陆
        2 查看授课课程
        3 选择授课课程
        4 查看课程学生
        5 修改学生分数
        q 退出程序
        ''')
        choice = input('请选择功能：').strip()
        if choice == 'q':
            break
        if choice not in teacher_dic:continue
        teacher_dic[choice]()




