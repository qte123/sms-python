# 修改密码
from django.db import transaction
from datetime import datetime

from common.models import User
from common.utils.jsonUtils import get_json


def modify_password(request):
    info = request.params['data']
    try:
        with transaction.atomic():
            user = User.objects.get(username=info['username'], password=info['password'])
            user.password = info['old_password']
            user.modify_date = datetime.now()
    except User.DoesNotExist:
        return get_json({
            'ret': 1,
            'msg': '修改失败'
        })
    user.save()
    return get_json({
        'ret': 0,
        'msg': '修改成功'
    })
