# 选课功能处理
from django.db import transaction

from common.utils.handler import dispatcherBase
from common.utils.jsonUtils import get_json
from common.utils.querySetSlice import query_slice
# 导入 SC 对象定义
from common.models import SC, Student, Course
from common.utils.makeUUID import get_uuid
from datetime import datetime


def dispatcher(request):
    return dispatcherBase(request, Action2Handler, 'sc')


# 获取选课列表
def list_sc(request):
    # 返回一个QuerySet 对象，包含所有表记录
    pageIndex = request.POST.get('pageIndex')
    student_no = request.POST.get('student_no')
    if student_no == '':
        qs = query_slice(SC.objects.filter(is_show=1).values(), int(pageIndex))
        list1 = list(qs)
        r = []
        for sc in list1:
            student_no = sc['student_no_id']
            course_no = sc['course_no_id']
            student = Student.objects.get(no=student_no)
            course = Course.objects.get(no=course_no)
            if student.is_show == 0 or course.is_show == 0:
                sc.is_show = 0
            r.append(sc)
        retlist = r
    else:
        q = query_slice(Student.objects.filter(is_show=1, no__contains=student_no).values(), int(pageIndex))
        l = list(q)
        nl = []
        for s in l:
            sno = s['no']
            sc = SC.objects.get(student_no_id=sno)
            nl.append(sc)
        retlist = nl
    # 将QuerySet对象转化为list字符串
    # 否则不能转化为JSON字符串
    new_list = []
    for sc in retlist:
        sno = sc['student_no_id']
        cno = sc['course_no_id']
        student = Student.objects.get(no=sno)
        course = Course.objects.get(no=cno)
        new_dict = {'student_no': student.no, 'student_name': student.name, 'course_name': course.name,
                    'grade': sc['grade']}
        new_list.append(new_dict)
    return get_json({'ret': 0, 'retlist': new_list})


# 添加成绩
def add_sc(request):
    student_no = request.POST.get('student_no')
    course_name = request.POST.get('course_name')
    grade = request.POST.get('grade')
    # 从请求消息中，获取要添加选课的信息
    # 并且插入到数据库中
    try:
        with transaction.atomic():
            student = Student.objects.get(no=student_no)
            course = Course.objects.get(name=course_name)
            record = SC.objects.create(uuid=get_uuid(), student_no_id=student.no, course_no_id=course.no, grade=grade,
                                       create_date=datetime.now())
    except Exception:
        return get_json({'ret': 1, 'msg': '添加失败'})
    return get_json({'ret': 0, 'msg': '添加成功'})


# 修改选课
def modify_sc(request):
    # 从请求消息中，获取修改选课的信息
    # 找到该信息，并且进行修改操作
    student_no = request.POST.get('student_no')
    course_name = request.POST.get('course_name')
    grade = request.POST.get('grade')
    try:
        # 根据Sno,Cno从数据库中找到相应的选课记录
        with transaction.atomic():
            course = Course.objects.get(name=course_name)
            sc = SC.objects.get(student_no_id=student_no, course_no_id=course.no)
    except SC.DoesNotExist:
        return get_json({'ret': 1, 'msg': '修改失败'})
    sc.grade = grade
    sc.modify_date = datetime.now()
    # 注意，一定要执行save才能将修改信息保存到数据库里
    sc.save()
    return get_json({'ret': 0, 'msg': '修改成功'})


# 删除选课
def delete_sc(request):
    student_no = request.POST.get('student_no')
    course_name = request.POST.get('course_name')
    try:
        # 根据Sno,Cno从数据库中找到相应的课程记录
        with transaction.atomic():
            course = Course.objects.get(name=course_name)
            sc = SC.objects.get(student_no_id=student_no, course_no_id=course.no)
            sc.is_show = 0
            sc.modify_date = datetime.now()
    except SC.DoesNotExist:
        return get_json({'ret': 1, 'msg': '删除失败'})
    sc.save()
    return get_json({'ret': 0, 'msg': '删除成功'})


Action2Handler = {
    'list_sc': list_sc,
    'add_sc': add_sc,
    'modify_sc': modify_sc,
    'delete_sc': delete_sc,
}
