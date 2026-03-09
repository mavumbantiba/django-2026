from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Subject)
class Subject(admin.ModelAdmin):
    list_display=('name',)

@admin.register(Students)
class Student(admin.ModelAdmin):
    list_display=('name',)
