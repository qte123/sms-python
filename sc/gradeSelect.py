# 查询成绩
from django.db import transaction

from common.models import Course, SC, Student
from common.utils.handler import dispatcherBase
from common.utils.jsonUtils import get_json


def dispatcher(request):
    return dispatcherBase(request, Action2Handler, 'select')


def grade_select(request):
    student_no = request.POST.get('student_no')
    course_name = request.POST.get('course_name')
    try:
        with transaction.atomic():
            student = Student.objects.get(no=student_no)
    except Student.DoesNotExist:
        return get_json({'ret': 1, 'msg': '学号不存在'})
    try:
        with transaction.atomic():
            course = Course.objects.get(name=course_name)
    except Course.DoesNotExist:
        return get_json({'ret': 1, 'msg': '课程名不存在'})
    try:
        with transaction.atomic():
            sc = SC.objects.get(student_no_id=student_no, course_no_id=course.no, is_show=1)
            student_no = sc.student_no
            course_no = sc.course_no
            student = Student.objects.get(no=student_no.no)
            course = Course.objects.get(no=course_no.no)
            if student.is_show == 0 or course.is_show == 0:
                return get_json({'ret': 1, 'msg': '无效数据'})
            else:
                grade = sc.grade
    except SC.DoesNotExist:
        return get_json({'ret': 1, 'msg': '查找失败'})
    return get_json({'ret': 0, 'msg': '查找成功', 'grade': grade})


Action2Handler = {
    'grade_select': grade_select
}
