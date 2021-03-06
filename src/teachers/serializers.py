from rest_framework import serializers

from .models import Teacher
from subjects.models import Subject


class TeacherSerializer(serializers.ModelSerializer):
    subjects = serializers.PrimaryKeyRelatedField(many=True, queryset=Subject.objects.all())

    class Meta:
        model = Teacher
        fields = ('id', 'name', 'country', 'student', 'subjects',)

    read_only_fields = ('id',)

    # def validate_name(self, value):
    #     qs = Teacher.objects.filter(name__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError('name already exists!')
    #     return value
