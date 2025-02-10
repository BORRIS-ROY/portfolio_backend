from django.urls import path
from .views import project_list

urlpatterns = [
    path('api/projects/', project_list, name='project_list_api'),
]
