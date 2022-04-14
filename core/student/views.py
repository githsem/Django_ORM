from django.shortcuts import render
from .models import Student, Teacher
from django.db import connection
from django.db.models import Q


def student_list1(request):
    posts = Student.objects.all()
    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

def student_list2(request):
    posts = Student.objects.filter(Q(surname__startswith = 'Yil') & ~Q(surname__startswith = 'k'))
    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

def student_list3(request):
    posts = Student.objects.all().values_list('firstname').union(Teacher.objects.all().values_list('firstname'))
    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})    

def student_list4(request):
    posts = Student.objects.filter(~Q(age__gt = 12))
    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})    

def student_list5(request):
    posts = Student.objects.filter(classroom = 6).only('firstname')
    print(posts)
    print(posts.query)
    print(connection.queries)
    return render(request, 'output.html',{'data':posts})      

def student_list(request):
    posts = Student.objects.raw("SELECT * FROM student_student WHERE age = 12")
    print(posts)
    print(posts.query)
    print(connection.queries)
    return render(request, 'output.html',{'data':posts})            
