from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages

# Create your views here.

def home(request):
    courses = Course.objects.all()
    return render(request, 'home.html', {'courses':courses})
# Path: courses/models.py
# Compare this snippet from university/settings.py:
# DEBUG = True

# ALLOWED_HOSTS = []

def registercourse(request):
    code=request.POST['txtcode']
    name=request.POST['txtname']
    credits=request.POST['txtcredits']
    
    Course = Course.objects.create(code=code, name=name, credits=credits)
    messages.success(request, '¡Registered course!')
    return redirect('/')

# Path: university/courses/templates/home.html
# Compare this snippet from university/courses/views.py:
def editionCurso(request, code):
    course = Course.objects.get(code=code)
    return render(request, "edition.html", {"course": course})

def editCurso(request):
    code = request.POST['txtCode']
    name = request.POST['txtName']
    credits = request.POST['numCredits']

    course = Course.objects.get(code=code)
    course.name = name
    course.credits = credits
    course.save()

    messages.success(request, '¡Updated course!')

    return redirect('/')

def deleteCurso(request, code):
    course = Course.objects.get(code=code)
    course.delete()

    messages.success(request, '¡Course removed!')

    return redirect('/')

