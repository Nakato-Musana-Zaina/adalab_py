from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher_age=models.PositiveSmallIntegerField()
    teacher_name=models.CharField(max_length=20)
    teacher_id=models.PositiveSmallIntegerField()
    teacher_course=models.CharField(max_length=20)
    teacher_class=models.CharField(max_length=20)
    teacher_description=models.CharField(max_length=20)
    teacher_occupation=models.CharField(max_length=20)
    teacher_salary=models.SmallIntegerField()
    teacher_hobby=models.CharField(max_length=20)
    teacher_picture=models.CharField(max_length=20)
    def __str__(self):
        return f'{self.teacher_description}'
