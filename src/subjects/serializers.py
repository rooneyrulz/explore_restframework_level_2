from rest_framework import serializers
from .models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name', 'teacher',)

    read_only_fields = ('id',)

    # def validate_name(self, value):
    #     qs = Teacher.objects.filter(name__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError('name already exists!')
    #     return value
