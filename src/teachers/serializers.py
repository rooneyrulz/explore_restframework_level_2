from rest_framework import serializers
from .models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'name', 'country', 'student',)

    read_only_fields = ('id',)

    # def validate_name(self, value):
    #     qs = Teacher.objects.filter(name__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError('name already exists!')
    #     return value
