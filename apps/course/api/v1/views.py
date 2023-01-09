from rest_framework import permissions, generics, status
from rest_framework.response import Response

from .serializers import CourseCreateSerializer, CourseGetSerializer, LessonGetSerializer, LessonPostSerializer
from ...models import Course, Lesson
from .permissions import IsOwnerOrReadOnly, IsOwnerForLessonOrReadOnly



class CourseListView(generics.ListAPIView):
    # http://127.0.0.1:8000/api/course/v1/list/
    queryset = Course.objects.all()
    serializer_class = CourseGetSerializer


class CourseCreateView(generics.CreateAPIView):
    # http://127.0.0.1:8000/api/course/v1/create/
    queryset = Course.objects.all()
    serializer_class = CourseCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        obj = self.queryset.get(id=serializer.data.get('id'))
        headers = self.get_success_headers(serializer.data)
        sz = CourseGetSerializer(obj)
        return Response(sz.data, status=status.HTTP_201_CREATED, headers=headers)


class CourseRUDView(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/api/course/v1/rud/<id>/
    queryset = Course.objects.all()
    serializer_class = None
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CourseGetSerializer
        return CourseCreateSerializer


class LessonListView(generics.ListAPIView):
    # http://127.0.0.1:8000/api/course/v1/course/<course_id>/lessons/list/
    queryset = Lesson.objects.all()
    serializer_class = LessonGetSerializer
    lookup_url_kwarg = 'course_id'

    def get_queryset(self):
        qs = super().get_queryset()
        course_id = self.kwargs.get(self.lookup_url_kwarg)
        qs = qs.filter(course_id=course_id)
        return qs


class LessonCreateView(generics.CreateAPIView):
    # http://127.0.0.1:8000/api/course/v1/course/<course_id>/lessons/create/
    queryset = Lesson.objects.all()
    serializer_class = LessonPostSerializer
    permission_classes = (IsOwnerForLessonOrReadOnly, permissions.IsAuthenticated)
    lookup_url_kwarg = 'course_id'

    def create(self, request, *args, **kwargs):
        course_id = self.kwargs.get(self.lookup_url_kwarg)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(course_id=course_id)
        obj = self.queryset.get(id=serializer.data.get('id'))
        headers = self.get_success_headers(serializer.data)
        sz = LessonGetSerializer(obj)
        return Response(sz.data, status=status.HTTP_201_CREATED, headers=headers)


class LessonRUDView(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/api/course/v1/course/<course_id>/lessons/rud/<id>/
    queryset = Lesson.objects.all()
    serializer_class = None
    permission_classes = (IsOwnerForLessonOrReadOnly, permissions.IsAuthenticated)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return LessonGetSerializer
        return LessonPostSerializer

