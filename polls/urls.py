from django.urls import path
from .views import (AllStudentView,DetailStudentView,
                    GetByEmailStudentView,CreateStudetView,
                    UpdateStudentView,DeleteStudentView)


urlpatterns = [
    path('get_all/',AllStudentView.as_view()),
    path('get_by_index/<int:student_id>',DetailStudentView.as_view()),
    path('get_by_email/<str:email>',GetByEmailStudentView.as_view()),

    path('create/',CreateStudetView.as_view()),
    path('update/<int:student_id>/',UpdateStudentView.as_view()),
    path('delete/<int:student_id>/',DeleteStudentView.as_view()),
]
