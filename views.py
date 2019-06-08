from django.shortcuts import render
from .models import *
from django.urls import *

# Create your views here.
def index(request):
    return render(request,'Welcome to our community',context)

def user(request):
    sign=User.object.all()
    return render(request,"Join and have fun")

def listSkills (request):
    Skills=Skill.object.all()

    return render(request,"The List")


def showProfile (reqest):
    Volunteers=Volunteer.object.all()

    return render(reqest,"Hi this is ..")

def comment (request):
    Comments=Comment.object.all()

    return render(request,"Leave your comment")

