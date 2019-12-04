from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404

from .models import Subject
from .serializers import SubjectSerializer


class SubjectListCreateAPIView(APIView):
    serializer = SubjectSerializer

    def get(self, request, id=None, *args, **kwargs):
        qs = Subject.objects.all()
        serializer = self.serializer(qs, many=True)
        return Response(data=serializer.data, status=HTTP_200_OK)

    def post(self, request, id=None, *args, **kwargs):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=HTTP_201_CREATED)


class SubjectObjectMixin(object):
    def get_object(self, id, *args, **kwargs):
        return get_object_or_404(Subject, pk=id)


class SubjectRetrieveUpdateDeleteAPIView(SubjectObjectMixin, APIView):
    serializer = SubjectSerializer

    def get(self, request, id, *args, **kwargs):
        obj = self.get_object(id)
        serializer = self.serializer(obj, many=False)
        return Response(data=serializer.data, status=HTTP_200_OK)

    def put(self, request, id, *args, **kwargs):
        obj = self.get_object(id)
        serializer = self.serializer(obj, data=request.data, many=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=HTTP_200_OK)

    def delete(self, request, id, *args, **kwargs):
        obj = self.get_object(id)
        obj.delete()
        return Response(data='subject deleted!', status=HTTP_200_OK)

