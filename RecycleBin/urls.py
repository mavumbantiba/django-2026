"""
URL configuration for RecycleBin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Bin.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-subject', add_subject, name='add-subject'),
    path('', home, name='home'),
    path('add-student',add_student,name='add-student'),
    path('actions',recyclebin_actions,name='actions'),
    path('student/<int:id>', student_details, name='student-details'),
    path('delete',delete,name='delete'),
    path('recyclebin',recycle_bin, name='recyclebin'),
    path('student/delete-student/<int:id>', delete_student_byID, name='delete-student')
]
