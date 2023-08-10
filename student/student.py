# 学生功能处理
from django.db import transaction

# 导入 SC 对象定义
from common.models import Student
from common.utils.handler import dispatcherBase
from common.utils.jsonUtils import get_json
from common.utils.querySetSlice import query_slice
from common.utils.makeUUID import get_uuid
from datetime import datetime


def dispatcher(request):
    return dispatcherBase(request, Action2Handler, 'student')


# 获取学生列表
def list_student(request):
    # 返回一个QuerySet 对象，包含所有表记录
    pageIndex = request.POST.get('pageIndex')
    no = request.POST.get('no')
    if no == '':
        qs = query_slice(Student.objects.filter(is_show=1).values(), int(pageIndex))
    else:
        qs = query_slice(Student.objects.filter(is_show=1, no__contains=no).values(), int(pageIndex))
    # 将QuerySet对象转化为list字符串
    # 否则不能转化为JSON字符串
    retlist = list(qs)
    return get_json({'ret': 0, 'retlist': retlist})


# 添加学生
def add_student(request):
    no = request.POST.get('no')
    name = request.POST.get('name')
    sex = request.POST.get('sex')
    age = request.POST.get('age')
    department = request.POST.get('department')
    print(department)
    # 从请求消息中，获取要添加学生的信息
    # 并且插入到数据库中
    try:
        with transaction.atomic():
            record = Student.objects.create(uuid=get_uuid(), no=no, name=name, sex=sex,
                                            age=age,
                                            department=department, create_date=datetime.now())
    except Exception:
        return get_json({'ret': 1, 'msg': '添加失败'})
    return get_json({'ret': 0, 'msg': '添加成功'})


# 修改学生
def modify_student(request):
    # 从请求消息中，获取修改学生的信息
    # 找到该信息，并且进行修改操作

    no = request.POST.get('no')
    name = request.POST.get('name')
    sex = request.POST.get('sex')
    age = request.POST.get('age')
    department = request.POST.get('department')
    try:
        # 根据Sno从数据库中找到相应的选课记录
        with transaction.atomic():
            student = Student.objects.get(no=no)
            student.name = name
            student.sex = sex
            student.age = age
            student.department = department
            student.modify_date = datetime.now()
    except Student.DoesNotExist:
        return get_json({'ret': 1, 'msg': '修改失败'})
    student.save()
    return get_json({'ret': 0, 'msg': '修改成功'})


# 删除学生
def delete_student(request):
    no = request.POST.get('no')
    try:
        # 根据Sno,Cno从数据库中找到相应的课程记录
        with transaction.atomic():
            student = Student.objects.get(no=no)
            student.is_show = 0
            student.modify_date = datetime.now()

    except Student.DoesNotExist:
        return get_json({'ret': 1, 'msg': '删除失败'})
    student.save()
    return get_json({'ret': 0, 'msg': '删除成功'})


Action2Handler = {
    'list_student': list_student,
    'add_student': add_student,
    'modify_student': modify_student,
    'delete_student': delete_student,
}
