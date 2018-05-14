
from lib import common
from interface import common_interface,admin_interface

admin_info = {
    'name':None
}

def login():
    while True:
        name = input('请输入用户名:').strip()
        password = input('请输入密码:').strip()
        flag,msg = common_interface.login_interface(name,password,'admin')
        if flag:
            print(msg)
            admin_info['name'] = name
            break
        else:
            print(msg)



def register():
    while True:
        name = input('请输入用户名:').strip()
        password = input('请输入密码:').strip()
        conf_password = input('请确认密码:').strip()
        if password == conf_password:
            flag,msg = admin_interface.register_interface(name,password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print("密码不一致!")


@common.auth_login(type='admin')
def create_school():
    while True:
        school_name = input('请输入学校名字:').strip()
        address = input('请输入学校地址:').strip()
        if school_name == 'q':break
        if address == 'q':break
        flag,msg = admin_interface.create_school_interface(admin_info['name'],school_name,address)
        if flag:
            print(msg)
            break
        else:
            print(msg)

@common.auth_login(type='admin')
def create_course():
    while True:
        school_list = common.check_files('school')
        for i,school in enumerate(school_list):
            print('%s   %s' %(i,school))
        choice = input('请选择学校:').strip()
        if choice == 'q':break
        if choice.isdigit():
            choice = int(choice)
            if choice < len(school_list):
                course_name = input('请输入课程名称:').strip()
                if course_name == 'q': break
                flag,msg = admin_interface.create_course_interface(admin_info['name'],school_list[choice],course_name)
                if flag:
                    print(msg)
                    break
                else:
                    print(msg)
            else:
                print('请输入课程编号!')
        else:
            print('请输入数字!')

@common.auth_login(type='admin')
def create_teacher():
    while True:
        teacher_name = input('请输入老师名字:').strip()
        if teacher_name == 'q':break
        flag,msg = admin_interface.create_teacher_interface(admin_info['name'],teacher_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)


admin_dic = {
    '1':login,
    '2':register,
    '3':create_school,
    '4':create_course,
    '5':create_teacher
}




def admin_view():
    while True:
        print('''
        1 管理员登陆
        2 管理员注册
        3 创建学校
        4 创建课程
        5 创建老师
        q 退出程序
        ''')
        choice = input('请选择功能:').strip()
        if choice == 'q':break
        if choice not in admin_dic:continue
        admin_dic[choice]()
