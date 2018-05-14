
from lib import common
from interface import common_interface,student_interface
student_info = {
    'name':None
}

def login():
    while True:
        name = input('请输入用户名:').strip()
        password = input('请输入密码:').strip()
        flag,msg = common_interface.login_interface(name,password,'student')
        if flag:
            print(msg)
            student_info['name'] = name
            break
        else:
            print(msg)



def register():
    while True:
        name = input('请输入用户名:').strip()
        password = input('请输入密码:').strip()
        conf_password = input('请确认密码:').strip()
        if password == conf_password:
            flag,msg = student_interface.register_interface(name,password)
            if flag:
                print(msg)
                break
            else:
                print(msg)


@common.auth_login(type='student')
def choice_school():
    while True:
        school_list = common.check_files('school')
        for i,school in enumerate(school_list):
            print('%s   %s' %(i,school))
        choice = input('请选择学校:').strip()
        if choice.isdigit():
            choice = int(choice)
            if choice < len(school_list):
                flag,msg = student_interface.choice_school_interface(student_info['name'],school_list[choice])
                if flag:
                    print(msg)
                    break
                else:
                    print(msg)
            else:
                print(' 请选择学校编号!')
        else:
            print('必须为数字！')



@common.auth_login(type='student')
def choice_course():
    while True:
        course_list = student_interface.get_student_school_course(student_info['name'])
        for i,course in enumerate(course_list):
            print('%s  %s' %(i,course))
        choice  = input('请选择课程:').strip()
        if choice.isdigit():
            choice = int(choice)
            if choice < len(course_list):
                flag,msg = student_interface.choice_course_interface(student_info['name'],course_list[choice])
                if flag:
                    print(msg)
                    break
                else:
                    print(msg)
            else:
                print('请输入编号！')
        else:
            print('必须为数字！')







@common.auth_login(type='student')
def check_score():
    score  = student_interface.check_score(student_info['name'])
    print(score)




student_dic = {
    '1':login,
    '2':register,
    '3':choice_school,
    '4':choice_course,
    '5':check_score

}

def student_view():
    while True:
        print('''
        1 学生登陆
        2 学生注册
        3 选择学校
        4 选择课程
        5 查看分数
        q 退出程序
        ''')
        choice = input('请选择功能').strip()
        if choice == 'q':break
        if choice not in student_dic:
            continue
        student_dic[choice]()













