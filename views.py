from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render




def demofunction(request):
    return HttpResponse("<h2 align=center>Hello World..!<h2>")


def demofunction1(request):
    return HttpResponse("<H2>Student Learning Management System</H2>")


def demofunction2(request):
    return HttpResponse("<font color='green'><H1>MySDP Project</H1></font>")


def homefunction(request):
    return render(request, "index.html")


def aboutfunction(request):
    return render(request, "about.html")


def loginfunction(request):
    return render(request, "login.html")

def facultylogin(request):
    return render(request, "facultylogin.html")

def studentlogin(request):
    return render(request, "studentlogin.html")

def contactfunction(request):
    return render(request, "contact.html")









