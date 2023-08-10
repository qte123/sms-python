# 课程功能处理
from django.db import transaction

from common.utils.handler import dispatcherBase
from common.utils.jsonUtils import get_json
from common.utils.querySetSlice import query_slice
# 导入 Course 对象定义
from common.models import Course
from common.utils.makeUUID import get_uuid
from datetime import datetime


def dispatcher(request):
    return dispatcherBase(request, Action2Handler, 'course')


# 获取课程列表
def list_course(request):
    # 返回一个QuerySet 对象，包含所有表记录
    pageIndex = request.POST.get('pageIndex')
    name = request.POST.get('name')
    if name == '':
        qs = query_slice(Course.objects.filter(is_show=1).values(), int(pageIndex))
    else:
        qs = query_slice(Course.objects.filter(is_show=1, name__contains=name).values(), int(pageIndex))
    # 将QuerySet对象转化为list字符串
    # 否则不能转化为JSON字符串
    retlist = list(qs)
    return get_json({'ret': 0, 'retlist': retlist})


# 添加课程
def add_course(request):
    no = request.POST.get('no')
    name = request.POST.get('name')
    pno = request.POST.get('pno')
    credit = request.POST.get('credit')
    # 从请求消息中，获取要添加课程的信息
    # 并且插入到数据库中
    try:
        with transaction.atomic():
            record = Course.objects.create(uuid=get_uuid(), no=no, name=name, pno=pno,
                                           credit=credit, create_date=datetime.now())
    except Exception:
        return get_json({'ret': 1, 'msg': '添加失败'})
    return get_json({'ret': 0, 'msg': '添加成功'})


# 修改课程
def modify_course(request):
    # 从请求消息中，获取修改课程的信息
    # 找到该课程，并且进行修改操作
    no = request.POST.get('no')
    name = request.POST.get('name')
    pno = request.POST.get('pno')
    credit = request.POST.get('credit')

    try:
        # 根据Cno从数据库中找到相应的课程记录
        with transaction.atomic():
            course = Course.objects.get(no=no)
            course.name = name
            course.pno = pno
            course.credit = credit
            course.modify_date = datetime.now()
    except Course.DoesNotExist:
        return get_json({'ret': 1, 'msg': '修改失败'})
    # 注意，一定要执行save才能将修改信息保存到数据库里
    course.save()
    return get_json({'ret': 0, 'msg': '修改成功'})


# 删除课程
def delete_course(request):
    name = request.POST.get('name')
    try:
        # 根据Cno从数据库中找到相应的课程记录
        with transaction.atomic():
            course = Course.objects.get(name=name)
            course.is_show = 0
            course.modify_date = datetime.now()
    except Course.DoesNotExist:
        return get_json({'ret': 1, 'msg': '删除失败'})
    course.save()
    return get_json({'ret': 0, 'msg': '删除成功'})


Action2Handler = {
    'list_course': list_course,
    'add_course': add_course,
    'modify_course': modify_course,
    'delete_course': delete_course,
}
