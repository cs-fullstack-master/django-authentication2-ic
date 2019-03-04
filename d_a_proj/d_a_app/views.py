from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def all_classes(request):
    return HttpResponse('all classes')

def my_classes(request):
    return HttpResponse('my classes')


