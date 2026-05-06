from django.urls import path
from . import views

urlpatterns = [
    path('', views.exam_list, name='home'),
    path('exams/', views.exam_list, name='exam_list'),
    path('exams/<int:exam_id>/take/', views.take_exam, name='take_exam'),
    path('results/<int:submission_id>/', views.exam_result, name='exam_result'),
]
