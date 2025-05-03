from django.contrib import admin
from django.urls import path
from erp import views

urlpatterns = [
    path('category/create/',views.CategoryListCreateApiView.as_view(),name='create_category'),
    path('category/detail/<int:pk>/',views.CategoryDetailAPiView.as_view(),name='category_detail'),
    path('course/create/',views.CourseListCreateApiView.as_view(),name='course_create'),
    # Student urls
    path('students/',views.StudentGenericApiView.as_view(),name='students'),
    path('courses/<int:category_id>/',views.CourseListByCategory.as_view(),name='course_list_by_category'),
    path('homework/create/',views.HomeworkCreateAPIView.as_view(),name='hmw_create'),
]