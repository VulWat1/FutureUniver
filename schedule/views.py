from django.shortcuts import render
from rest_framework import viewsets
from .models import ScheduleCell, Group, Teacher, Subject
from .serializers import ScheduleCellSerializer, GroupSerializer, TeacherSerializer, SubjectSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "schedule/index.html"


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class ScheduleCellViewSet(viewsets.ModelViewSet):
    queryset = ScheduleCell.objects.all()
    serializer_class = ScheduleCellSerializer


class CellViewSet(viewsets.ModelViewSet):
    queryset = ScheduleCell.objects.all()
    serializer_class = ScheduleCellSerializer