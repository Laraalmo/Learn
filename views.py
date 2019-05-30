from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request,'Welcome to our community',context)


def listSkills (request):
    Skills=Skill.object.all()



