from rest_framework import permissions
from edu.perimissions import IsAdminOrReadOnly, IsTeacherOrReadOnly
from typing import FrozenSet
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import render,get_object_or_404
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import *
from .models import *
from .serializers import *
from rest_framework.permissions import *
from .perimissions import *


class DayListView(ListCreateAPIView):
    serializer_class = DaySerializer
    queryset = Day.objects.all()
    permission_classes = [IsAdminUser]
    

class DayDetailListView(RetrieveUpdateDestroyAPIView):
    serializer_class = DaySerializer
    queryset = Day.objects.all()
    permission_classes = [IsAdminUser]



class SubjectListView(ListCreateAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAdminOrReadOnly, IsTeacherOrReadOnly]


class SubjectLessonListView(ListAPIView):
    serializer_class = SubjectLessonSerializer
    queryset = Subject.objects.all()


class TeacherListView(ListCreateAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    permission_classes = [HasProfile, IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class TeacherDetailListView(ListAPIView):
    serializer_class = TeacherDetailSerializer
    queryset = Teacher.objects.all()
    permission_classes = [IsAdminUser]



class GroupListView(ListCreateAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = [IsAuthenticated,IsTeacherOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(teachers=self.request.user)


class StudentListView(ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = [IsTeacherOrReadOnly,IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)



class StudentWaitingView(ListAPIView):
    serializer_class = StudentWaitingSerializer
    queryset = Student.objects.filter(status="waiting")



@api_view(["POST"])
@permission_classes([IsOwnerOrReadOnly, IsTeacherOrReadOnly, IsAdminUser])
def JoinStudentGroup(request):
    try:
        if request.method == "POST":
            data = request.data
            group = get_object_or_404(Group,id=data["group"])
            for id in data["list"]:
                student = get_object_or_404(Student, id=id)
                student.status = "active"
                student.save()
                group.students.add(student)
            return Response({"xatolik":"Muvaffaqiyatli qo'shildi!"})
    except:
        return Response({"xatolik":"Student qo'shishda xatolik yuz berdi!"})



