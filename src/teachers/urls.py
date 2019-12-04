from django.urls import path
from .views import TeacherListCreateAPIView, TeacherRetrieveUpdateDeleteAPIView


app_name = 'teachers'
urlpatterns = [
    path('', TeacherListCreateAPIView.as_view(), name='teacher-list'),
    path('<int:id>', TeacherRetrieveUpdateDeleteAPIView.as_view(), name='teacher-retrieve'),
]
