# 实体
import datetime

from django.db import models


# 用户
class User(models.Model):
    # uuid
    uuid = models.CharField(max_length=50)
    # 用户名
    username = models.CharField(max_length=9, primary_key=True)
    # 密码
    password = models.CharField(max_length=20, null=False, blank=False)
    # 最近登录时间
    last_login = models.DateTimeField(default=datetime.datetime.now())
    # 创建时间
    create_date = models.DateTimeField(null=True)
    # 修改时间
    modify_date = models.DateTimeField(null=True)
    # 用户类型 0学生 1老师 2管理员
    user_type = models.PositiveSmallIntegerField(default=0)
    # 是否激活  0是停用，1是激活
    is_activate = models.PositiveSmallIntegerField(default=1)
    # 是否隐藏 0是已隐藏，1是未隐藏
    is_show = models.PositiveSmallIntegerField(default=1)


# 学生
class Student(models.Model):
    # uuid
    uuid = models.CharField(max_length=50)
    # 学号
    no = models.CharField(max_length=9, primary_key=True)
    # 姓名
    name = models.CharField(max_length=20, null=False, blank=False)
    # 性别
    sex = models.CharField(max_length=2, default='男')
    # 年龄
    age = models.PositiveSmallIntegerField(null=False, blank=False)
    # 院系
    department = models.CharField(max_length=20, null=False, blank=False)
    # 创建时间
    create_date = models.DateTimeField(null=True)
    # 修改时间
    modify_date = models.DateTimeField(null=True)
    # 是否隐藏 0是已隐藏，1是未隐藏
    is_show = models.PositiveSmallIntegerField(default=1)


# 课程
class Course(models.Model):
    # uuid
    uuid = models.CharField(max_length=50)
    # 课程号
    no = models.CharField(max_length=4, primary_key=True)
    # 课程名
    name = models.CharField(max_length=40, null=False, blank=False)
    # 该课程的先修课程
    pno = models.CharField(max_length=4)
    # 学分
    credit = models.PositiveSmallIntegerField(null=False, blank=False)
    # 创建时间
    create_date = models.DateTimeField(null=True)
    # 修改时间
    modify_date = models.DateTimeField(null=True)
    # 是否激活  0是停用，1是激活
    is_activate = models.PositiveSmallIntegerField(default=1)
    # 是否隐藏 0是已隐藏，1是未隐藏
    is_show = models.PositiveSmallIntegerField(default=1)


# 选课
class SC(models.Model):
    # uuid
    uuid = models.CharField(max_length=50, primary_key=True)
    # 学号
    student_no = models.ForeignKey(Student, on_delete=models.PROTECT)
    # 课程号
    course_no = models.ForeignKey(Course, on_delete=models.PROTECT)
    # 成绩
    grade = models.PositiveSmallIntegerField(default=0)
    # 创建时间
    create_date = models.DateTimeField(null=True)
    # 修改时间
    modify_date = models.DateTimeField(null=True)
    # 是否隐藏 0是已隐藏，1是未隐藏
    is_show = models.PositiveSmallIntegerField(default=1)
