from django.shortcuts import render
from django.contrib.auth import authenticate,login
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        return render(request,"index.html")
    elif request.method == 'GET':
        return render(request, "login.html",{})


