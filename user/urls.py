from django.urls import path
from user import user
from user import login_out
from user import modfiyPassword
from user import register

urlpatterns = [
    path('do/', user.dispatcher),
    path('login/', login_out.login),
    path('logout/', login_out.logout),
    path('modify_password/', modfiyPassword.modify_password),
    path('register/', register.register)
]
