from django.urls import path
from .views import add_course, add_instance, list_courses, list_instances

urlpatterns = [
    path('add_course/', add_course, name='add_course'),
    path('add_instance/', add_instance, name='add_instance'),
    path('list_courses/', list_courses, name='list_courses'),
    path('list_instances/', list_instances, name='list_instances'),
]