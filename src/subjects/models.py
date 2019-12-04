from django.db import models
from teachers.models import Teacher


class Subject(models.Model):
    name = models.CharField(max_length=120)
    teacher = models.ForeignKey(Teacher, related_name='subjects', on_delete=models.SET_NULL)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self, *args, **kwargs):
        return self.name
