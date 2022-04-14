from django.shortcuts import render
from .models import Student


def student_list(request):

    posts = Student.objects.all()

    return render(request, 'output.html',{'posts':posts})