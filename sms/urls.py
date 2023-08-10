from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/user/', include('user.urls')),
                  path('api/student/', include('student.urls')),
                  path('api/course/', include('course.urls')),
                  path('api/sc/', include('sc.urls')),
                  path('sms/', include('app.urls')),
                  path('sms/html/root/', include('common.urls'))
              ] + static("/", document_root='./templates')
