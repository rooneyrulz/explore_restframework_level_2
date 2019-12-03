from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self, *args, **kwargs):
        return self.name
