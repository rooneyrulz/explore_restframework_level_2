from django.urls import path
from .views import TeacherListCreateAPIView


app_name = 'teachers'
urlpatterns = [
    path('', TeacherListCreateAPIView.as_view(), name='teacher-list'),
]
