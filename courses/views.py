from django.shortcuts import render, redirect
from .models import Course, CourseInstance
from .forms import CourseForm, CourseInstanceForm

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_courses')
    else:
        form = CourseForm()
    return render(request, 'courses/add_course.html', {'form': form})

def add_instance(request):
    if request.method == 'POST':
        form = CourseInstanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_courses')
    else:
        form = CourseInstanceForm()
    return render(request, 'courses/add_instance.html', {'form': form})

def list_courses(request):
    courses = Course.objects.all()
    return render(request, 'courses/list_courses.html', {'courses': courses})

def list_instances(request):
    instances = CourseInstance.objects.all()
    return render(request, 'courses/list_instances.html', {'instances': instances})
