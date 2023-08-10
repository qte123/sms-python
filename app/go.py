from django.shortcuts import redirect, render


def go_login(request):
    return redirect('login.html')
