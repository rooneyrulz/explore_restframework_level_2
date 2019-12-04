from django.db import models
from students.models import Student


class Teacher(models.Model):
    name = models.CharField(max_length=120)
    country = models.CharField(max_length=120, blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self, *args, **kwargs):
        return self.name