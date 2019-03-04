from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import Course

@login_required
def all_classes(request):
    course_list = Course.objects.all()
    context = {'course_list': course_list}
    return render(request, 'd_a_app/all_classes.html', context)

@login_required
def my_classes(request):
    course_list = Course.objects.filter(course_teacher=request.user)
    context = {'course_list': course_list}
    return render(request, 'd_a_app/my_classes.html',context)


