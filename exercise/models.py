from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from student.models import Student


# Create your models here.

class Exercise(models.Model):
    title = models.CharField(max_length=50)
    material = RichTextUploadingField()
    template = models.TextField(default="",blank=True)
    test_case = models.TextField(default='',blank=True)
    problem_tree = models.TextField(default="",blank=True)
    complete_student = models.ManyToManyField(Student)


    def __str__(self):
        return self.title
