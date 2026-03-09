from django.shortcuts import render, redirect
from .models import *
from datetime import *
from django.contrib import messages
from django.db.models import Q
# Create your views here.

def home(request):
    user=request.user
    search_query=request.GET.get('q')
    if search_query:
        students=Students.objects.filter(Q(name__icontains=search_query))
        found=students.count()
        return render(request,'home.html',{'students':students,'found':found})
    else:
        students=Students.objects.all()
        found=students.count()
        return render(request,'home.html',{'students':students,'found':found,'user':user})


def delete(request):
   # student=Students.objects.get(id=id)
   # student.delete()
    #return redirect('home')
    if request.method=='POST':
        ids=request.POST.getlist('selected-items')
        if not ids:
            messages.error(request,'Nothing has been moved to trash. Please select by checking at least the box input then continue')
            return redirect('home')
            
        else:
            Students.objects.filter(id__in=ids).delete()
            messages.success(request,f'Student(s) has been moved to trash')
            return redirect('home')
           

def recyclebin_actions(request):
    if request.method=='POST':
        action=request.POST.get('action')
        ids=request.POST.getlist('selected-items')
        if not ids:
            messages.error(request,'Please select an item to delete it permanently')
            return redirect('recyclebin')

        if action=='delete':
            Students.deleted_objects.filter(id__in=ids).hard_delete()
            messages.success(request,'An item has been deleted permanently')
            return redirect('recyclebin')
    
        elif action=='restore':
            Students.deleted_objects.filter(id__in=ids).restore()
            messages.success(request,'An item has been restored')
            return redirect('recyclebin')

def delete_student_byID(request,id):
    student=Students.objects.get(id=id)
    student.delete()
    messages.success(request,f'Student {student.name} has been moved to the trash successfully')
    return redirect('home')

def recycle_bin(request):
    deleted=Students.deleted_objects.all()
    total=deleted.count()
    return render(request,'recyclebin.html',{'deleted':deleted,'total':total})

def student_details(request,id):
    student=Students.objects.get(id=id)
    return render(request,'student-details.html',{'student':student})

def add_student(request):
    students=Students.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        if name is None:
            messages.error(request,'Please enter the valid name')
            return render(request,'add-student.html')
        
        elif len(name) <8:
            messages.error(request,'The valid name must be at least 3 characters long')
            return render(request,'add-student.html')
    
        elif name in [student.name for student in students]:
            messages.info(request,f'Student {name} has been already registered. Please enter the new name or modify the existing one')
            return render(request,'add-student.html')

        else:
            Students.objects.create(name=name)
            messages.success(request,f'Student {name} has been added successfully {datetime.now().strftime('%d-%m-%y  %I:%M %p')}')
            return redirect('home')
    return render(request,'add-student.html')

def add_subject(request):
    if request.method=='POST':
        name=request.POST.getlist('name')
        if not name:
            messages.error(request,'Please select at least one subject before submitting')
            return render(request,'add-subject.html')
            
        else:
            Subject.objects.create(name=name)
            messages.success(request,f'Subject {name} has been added successfully')
            return redirect('add-subject')
    return render(request,'add-subject.html')


def create_student(request):
    classes=Classroom.objects.all()

    if request.method=='POST':
        name=request.POST.get('name')
        number=request.POST.get('number')
        level=request.POST.get('level')







