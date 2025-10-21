from rest_framework import serializers
from .models import ScheduleCell, Group, Teacher, Subject

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class ScheduleCellSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source='subject.name', read_only=True)
    teacher_name = serializers.CharField(source='teacher.name', read_only=True)
    class Meta:
        model = ScheduleCell
        # fields = '__all__'
        fields = ['id', 'day', 'group', 'subject', 'teacher', 'time', 'subject_name', 'teacher_name']