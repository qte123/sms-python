# 登录处理
from django.db import transaction
from datetime import datetime
from common.models import User
from common.utils.jsonUtils import get_json


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    # 创建user对象
    try:
        # 根据username,password从数据库中找到相应的用户记录
        with transaction.atomic():
            user = User.objects.get(username=username, password=password)
            # 在session存入用户类型
            user.last_login = datetime.now()
            request.session['username'] = username
            if user.user_type == 0:
                request.session['userType'] = 'student'
                request.session['level'] = 7
                type1 = 0
            elif user.user_type == 1:
                request.session['userType'] = 'teacher'
                request.session['level'] = 8
                type1 = 1
            else:
                request.session['userType'] = 'admin'
                request.session['level'] = 9
                type1 = 2
        user.save()
    except User.DoesNotExist:
        return get_json({'ret': 1, 'msg': '用户名或密码错误'})
    return get_json({'ret': 0, 'msg': '登录成功', 'type': type1})


# 登出处理
def logout(request):
    request.session.delete()  # 删除session
    return get_json({'ret': 0, 'msg': '退出成功'})
