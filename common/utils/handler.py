from django.shortcuts import render, redirect

from common.models import User
from common.utils.jsonUtils import get_json, load_json


def dispatcherBase(request, action2HandlerTable, usertype):
    student = ['select']
    teacher = ['student', 'course', 'sc', 'select']
    admin = ['student', 'course', 'sc', 'user', 'select']
    handle_filter(request, student, teacher, admin, usertype, 0)

    # # GET 请求 参数 在request 对象的GET属性中
    # if request.mothod == 'GET':
    #     request.params = request.GET
    # elif request.mothod in ['POST', 'PUT', 'DELETE']:
    #     # 根据接口，POST/PUT/DELETE 请求的消息体都是json格式
    #     request.params = load_json(request)

    # 根据不同的action分派给不同的函数进行处理

    action = request.POST.get('action')
    if action in action2HandlerTable:
        handlerFunc = action2HandlerTable[action]
        return handlerFunc(request)

    else:
        return get_json({'ret': 1, 'msg': 'action参数错误'})


def handle_filter(request, student, teacher, admin, type, is_html):
    if is_html == 0:
        # 根据session判断用户是否能登录的管理员用户
        if 'userType' not in request.session:
            return get_json({'ret': 302, 'msg': '未登录', })
        username = request.session['username']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return get_json({'ret': 302, 'msg': '用户名不存在', })
        # 用户访问权限范围
        if (user.user_type == 0 and type not in student) or (
                user.user_type == 1 and type not in teacher) or (
                user.user_type == 2 and type not in admin):
            return get_json({'ret': 302, 'msg': '无权限访问'})
    else:
        # 根据session判断用户是否能登录的管理员用户
        if 'userType' not in request.session:
            return render(request, 'sms/html/root/error.html')
        username = request.session['username']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return render(request, 'sms/html/root/error.html')
        # 用户访问权限范围
        if (user.user_type == 0 and type not in student) or (
                user.user_type == 1 and type not in teacher) or (
                user.user_type == 2 and type not in admin):
            return render(request, 'sms/html/root/error.html')
        return render(request, request.path[1:])
