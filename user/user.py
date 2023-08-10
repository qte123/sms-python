from django.db import transaction

from common.models import User
from common.utils.handler import dispatcherBase
from common.utils.jsonUtils import get_json
from common.utils.querySetSlice import query_slice
from datetime import datetime


def dispatcher(request):
    return dispatcherBase(request, Action2Handler, 'user')


# 获取用户列表
def list_user(request):
    pageIndex = request.POST.get('pageIndex')
    username = request.POST.get('username')
    usertype = request.POST.get('usertype')
    if username == '' and usertype == '':
        qs = query_slice(User.objects.filter(is_show=1).values(), int(pageIndex))
    elif username != '' and usertype == '':
        qs = query_slice(User.objects.filter(is_show=1, username__contains=username).values(), int(pageIndex))
    elif username == '' and usertype != '':
        qs = query_slice(User.objects.filter(is_show=1, user_type=usertype).values(), int(pageIndex))
    else:
        qs = query_slice(User.objects.filter(is_show=1, user_type=usertype, username__contains=username).values(),
                         int(pageIndex))
    # 返回一个QuerySet 对象，包含所有表记录

    # 将QuerySet对象转化为list字符串
    # 否则不能转化为JSON字符串
    retlist = list(qs)
    return get_json({'ret': 0, 'retlist': retlist})


# 修改状态
def modify_status(request):
    # 从请求消息中，获取修改课程的信息
    # 找到该课程，并且进行修改操作
    username = request.POST.get('username')
    status = request.POST.get('status')
    try:
        # 根据Cno从数据库中找到相应的课程记录
        with transaction.atomic():
            username1 = request.session['username']
            user1 = User.objects.get(username=username1)
            if user1.user_type != 2:
                return get_json({'ret': 1, 'msg': '非管理员'})
            if user1.username != username:
                user = User.objects.get(username=username)
                if status == "activate":
                    user.is_activate = 1
                else:
                    user.is_activate = 0
                user.modify_date = datetime.now()
            else:
                return get_json({'ret': 1, 'msg': '修改的账号正在使用'})
    except User.DoesNotExist:
        return get_json({'ret': 1, 'msg': '修改失败'})
    # 注意，一定要执行save才能将修改信息保存到数据库里
    user.save()
    return get_json({'ret': 0, 'msg': '修改成功'})


# 用户删除
def delete_user(request):
    username = request.POST.get('username')
    try:
        # 根据Cno从数据库中找到相应的课程记录
        with transaction.atomic():
            username1 = request.session['username']
            user1 = User.objects.get(username=username1)
            if user1.user_type != 2:
                return get_json({'ret': 1, 'msg': '非管理员'})
            if user1.username != username:
                user = User.objects.get(username=username)
                user.is_show = 0
                user.modify_date = datetime.now()
            else:
                return get_json({'ret': 1, 'msg': '修改的账号正在使用'})
    except User.DoesNotExist:
        return get_json({'ret': 1, 'msg': '删除失败'})
    user.save()
    return get_json({'ret': 0, 'msg': '删除成功'})


Action2Handler = {
    'list_user': list_user,
    'modify_status': modify_status,
    'delete_user': delete_user,
}
