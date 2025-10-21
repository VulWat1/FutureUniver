from django.contrib import admin
from .models import Group, Teacher, Subject, ScheduleCell

# Регистрация простой модели
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

# Расписание с фильтрами и отображением важных полей
@admin.register(ScheduleCell)
class ScheduleCellAdmin(admin.ModelAdmin):
    list_display = ('id', 'day', 'period', 'group', 'subject', 'teacher', 'time')
    list_filter = ('day', 'group', 'subject', 'teacher')
    search_fields = ('group__name', 'subject__name', 'teacher__name')
    ordering = ('day', 'period', 'group')
