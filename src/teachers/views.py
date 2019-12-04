from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404

from .models import Teacher
from .serializers import TeacherSerializer


class TeacherListCreateAPIView(APIView):
    serializer = TeacherSerializer

    def get(self, request, id=None, *args, **kwargs):
        qs = Teacher.objects.all()
        serializer = self.serializer(qs, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)

    def post(self, request, id=None, *args, **kwargs):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=HTTP_201_CREATED)
