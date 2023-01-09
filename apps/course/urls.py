from django.urls import path
from .views import course_view, add_course
app_name = 'course'

urlpatterns = [
    path('', course_view, name='list'),
    path('add-course/', add_course, name='add_course'),
]
