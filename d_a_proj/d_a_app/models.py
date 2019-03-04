from django.contrib.auth.models import User

# Create your models here.
from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_description = models.CharField(max_length=500)
    course_credits = models.PositiveSmallIntegerField()
    course_teacher = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
