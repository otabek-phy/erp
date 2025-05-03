from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, ListAPIView, \
    CreateAPIView
from rest_framework.views import APIView
from erp.models import Category, Course, Student, Homework
from .serializers import CategoryModelSerializer, CourseModelSerializer, StudentModelSerializer, HomeworkSerializer
from django.db.models import Count
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class CategoryListCreateApiView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        queryset = Category.objects.all().annotate(course_count=Count('courses'))
        return queryset


class CategoryDetailAPiView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    lookup_field = 'pk'


class CourseListCreateApiView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer


# class StudentApiView(APIView):
#     def get(self,request):
#         students = Student.objects.all()
#         serializers = StudentModelSerializer(students,many=True,context = {'request':request})
#         return Response(serializers.data)


class StudentGenericApiView(GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def get(self, request, *args, **kwargs):
        products = self.get_queryset()
        serializers = self.get_serializer(products, many=True)
        return Response(serializers.data)


# class CourseListByCategory(ListAPIView):
#     '''      version 1

#     serializer_class = CourseModelSerializer

#     def get_queryset(self):
#         category_id = self.kwargs.get('category_id')
#         queryset = Course.objects.filter(category = category_id)
#         return queryset
#     '''
#     serializer_class = CourseModelSerializer

#     def get_queryset(self):
#         category_id = self.request.query_params.get('category')
#         if category_id:
#             return Course.objects.filter(category = category_id)
#         return Course.objects.none()


class CourseListByCategory(GenericAPIView):
    serializer_class = CourseModelSerializer

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        if category_id:
            return Course.objects.filter(category=category_id)
        return Course.objects.none()

    def get(self, request):
        students = self.get_queryset()
        serializers = self.get_serializer(students, many=True)
        return Response(serializers.data)


# courses/1/


class HomeworkCreateAPIView(CreateAPIView):
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()

    def perform_create(self, serializer):
        return super().perform_create(serializer)




from rest_framework import viewsets
from .models import Homework
from .serializers import HomeworkSerializer
from .permissions import IsWithinWorkingHours


class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    permission_classes = [IsWithinWorkingHours]

