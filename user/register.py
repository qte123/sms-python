# 用户注册
from django.db import transaction
from datetime import datetime
from common.models import User
from common.utils.jsonUtils import get_json
from common.utils.makeUUID import get_uuid


def register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user_type = request.POST.get('type')
    flag = False
    if (username is not None and username != '') and (password is not None and password != ''):
        if user_type == 'student':
            usertype = 0
        else:
            usertype = 1
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            flag = True

        if flag:
            try:
                with transaction.atomic():
                    user1 = User.objects.create(uuid=get_uuid(), username=username, password=password,
                                                user_type=usertype, create_date=datetime.now())
                return get_json({'ret': 0, 'msg': '注册成功'})
            except Exception:
                return get_json({'ret': 1, 'msg': '注册失败'})
            user1.save()
        else:
            return get_json({'ret': 1, 'msg': '用户已存在'})
