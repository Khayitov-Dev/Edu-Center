from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import(
    Day,
    Subject,
    Teacher,
    Group,
    Student,
)


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["name"]
        model = Day



class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["name","days"]
        model = Subject


class SubjectLessonSerializer(serializers.ModelSerializer):
    days = SubjectSerializer(many=True)
    class Meta:
        fields = ["name","days"]
        model = Subject



class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["id","name","surname"]
        model = Teacher


class TeacherDetailSerializer(serializers.ModelSerializer):
    group = TeacherSerializer(many=True)
    class Meta:
        fields = ["name","surname","date_of_birth","photo","phone","address","subject","group"]
        model = Teacher


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["name","day","price","start","finish"]
        model = Group


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["name","surname","date_of_birth","photo","phone","address","group"]
        model = Student


class StudentWaitingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["name","surname"]
        model = Student