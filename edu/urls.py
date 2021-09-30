from django.urls import path
from .views import *

urlpatterns = [
    path('day-list/',DayListView.as_view()),
    path('day-list/<int:pk>/',DayDetailListView.as_view()),
    path('subject-list/',SubjectListView.as_view()),
    path('subject-list/<int:pk>/',SubjectLessonListView.as_view()),
    path('teacher-list/',TeacherListView.as_view()),
    path('teacher-list/<int:pk>/',TeacherDetailListView.as_view()),
    path('group-list/',GroupListView.as_view()),
    path('student-list/',StudentListView.as_view()),
    path('student-waiting/',StudentWaitingView.as_view()),
    path('student-add-list/',JoinStudentGroup),
]