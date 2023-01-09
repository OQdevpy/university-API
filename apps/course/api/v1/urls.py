from django.urls import path, include
from .views import CourseListView, CourseCreateView, CourseRUDView, LessonListView, LessonCreateView, LessonRUDView


urlpatterns = [
    path('list/', CourseListView.as_view()),
    path('create/', CourseCreateView.as_view()),
    path('rud/<int:pk>/', CourseRUDView.as_view()),
    path('course/<int:course_id>/lessons/list/', LessonListView.as_view()),
    path('course/<int:course_id>/lessons/create/', LessonCreateView.as_view()),
    path('course/<int:course_id>/lessons/rud/<int:pk>/', LessonRUDView.as_view()),
]
