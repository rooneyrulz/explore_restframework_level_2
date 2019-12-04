from rest_framework import serializers

from .models import Student
from teachers.models import Teacher


class StudentSerializer(serializers.ModelSerializer):
    teachers = serializers.PrimaryKeyRelatedField(many=True, queryset=Teacher.objects.all())

    class Meta:
        model = Student
        fields = ('id', 'name', 'age', 'country', 'teachers')
    
    read_only_fields = ('id',)

    # def validate_name(self, value):
    #     qs = Student.objects.filter(name__icontains=value)
    #     if qs.exists():
    #         raise serializers.ValidationError('name already exists!')
    #     return value
