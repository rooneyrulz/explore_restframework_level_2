from django.urls import path
from .views import SubjectListCreateAPIView, SubjectRetrieveUpdateDeleteAPIView

app_name = 'subjects'
urlpatterns = [
    path(
        '',
        SubjectListCreateAPIView.as_view(),
        name='subject-list'
    ),
    path(
        '<int:id>/',
        SubjectRetrieveUpdateDeleteAPIView.as_view(),
        name='subject-retrieve'
    )
]
