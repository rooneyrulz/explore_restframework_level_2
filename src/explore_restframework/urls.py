from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/students/', include('students.urls', namespace='students')),
    path('api/teachers/', include('teachers.urls', namespace='teachers')),
    path('api/subjects/', include('subjects.urls', namespace='subjects')),
]
