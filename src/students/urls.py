from django.urls import path
from .views import StudentListCreateAPIView, StudentRetrieveUpdateDeleteAPIView


app_name = 'students'
urlpatterns = [
    path('', StudentListCreateAPIView.as_view(), name='student-list'),
    path('<int:id>', StudentRetrieveUpdateDeleteAPIView.as_view(), name='student-retrieve')
]
