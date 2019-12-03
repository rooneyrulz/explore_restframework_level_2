from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'age', 'country',)

    
    # def create(self, validated_data, *args, **kwargs):
    #     student = self.save(**validated_data)
    #     return student

