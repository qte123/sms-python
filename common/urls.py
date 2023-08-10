from django.urls import path
from common.utils import filter

urlpatterns = [
    path('', filter.page_filter),
    path('CourseManagement.html', filter.page_filter),
    path('addCourse.html', filter.page_filter),
    path('modifyCourse.html', filter.page_filter),
    path('deleteCourse.html', filter.page_filter),
    path('SCManagement.html', filter.page_filter),
    path('addSC.html', filter.page_filter),
    path('modifySC.html', filter.page_filter),
    path('deleteSC.html', filter.page_filter),
    path('StuManagement.html', filter.page_filter),
    path('addStudent.html', filter.page_filter),
    path('modifyStudent.html', filter.page_filter),
    path('deleteStudent.html', filter.page_filter),
    path('user.html', filter.page_filter),
    path('modifyUser.html', filter.page_filter),
    path('deleteUser.html', filter.page_filter),
    path('grade.html', filter.page_filter),
    path('index.html', filter.page_filter)
]
