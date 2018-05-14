


from db import models

def login_interface(name,password,type):
    if type == 'admin':
        obj = models.Admin.get_by_name(name)
    elif type == 'student':
        obj = models.Student.get_by_name(name)

    elif type == 'teacher':
        obj = models.Teacher.get_by_name(name)

    else:
        return False,"请求错误！"

    if obj:
        if obj.password == password:
            return True,'登陆成功!'
        else:
            return False,'密码错误!'
    else:
        return False,'用户不存在！'