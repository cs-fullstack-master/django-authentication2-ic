from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def all_classes(request):
    return render(request, 'd_a_app/all_classes.html')

def my_classes(request):
    return render(request, 'd_a_app/my_classes.html')


