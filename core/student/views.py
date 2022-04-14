from django.shortcuts import render
from .models import Student
from django.db import connection
from django.db.models import Q


def student_list_(request):

    posts = Student.objects.all()

    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

def student_list(request):

    posts = Student.objects.filter(Q(surname__startswith = 'Yil') & Q(surname__startswith = 'y'))
    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})
