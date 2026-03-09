from django.db import models
from django_softdelete.models import *

class Students(SoftDeleteModel):
    name=models.CharField(max_length=100,unique=True)

    


class Subject(SoftDeleteModel):
    name=models.JSONField(default=list)




class Classroom(SoftDeleteModel):
    class_name=models.CharField(max_length=20)
    stream=models.CharField(max_length=1)

    def __str__(self):
        return f'{self.name} {self.stream}'
    

class Student(SoftDeleteModel):
    full_name=models.CharField(max_length=100)
    registration_number=models.CharField(max_length=50)
    level=models.ForeignKey(Classroom,on_delete=models.CASCADE)

    class Meta:
        ordering=['-full_name']
    
    def __Str__(self):
        return f'{self.full_name} {self.registration_number}'