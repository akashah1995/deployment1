from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 10:
            errors['name'] = "Course name must be longer than 10 Characters!"
        if len(postData['description']) < 15:
            errors['description'] = "Description must be longer than 15 Characters!"
        
        return errors


class Course(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()

# Create your models here.
