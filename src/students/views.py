from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404

from .models import Student
from .serializers import StudentSerializer


class StudentListCreateAPIView(APIView):
    serializer = StudentSerializer

    def get(self, request, id=None, *args, **kwargs):
        qs = Student.objects.all()
        serializer = self.serializer(qs, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)

    def post(self, request, id=None, *args, **kwargs):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=HTTP_201_CREATED)
        return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)


class StudentObjectMixin(object):
    def get_object(self, id, *args, **kwargs):
        return get_object_or_404(Student, pk=id)


class StudentRetrieveUpdateDeleteAPIView(StudentObjectMixin, APIView):
    serializer = StudentSerializer

    def get(self, request, id, *args, **kwargs):
        obj = self.get_object(id)
        serializer = self.serializer(obj, many=False)
        return Response(data=serializer.data, status=HTTP_200_OK)

    def put(self, request, id, *args, **kwargs):
        obj = self.get_object(id)
        serializer = self.serializer(obj, data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=HTTP_200_OK)
        return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, id, *args, **kwargs):
        obj = self.get_object(id)
        obj.delete()
        return Response(data='student deleted!', status=HTTP_200_OK)
        