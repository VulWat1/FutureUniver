from django.db import models
from django.utils.translation import gettext_lazy as _

class Group(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Топтун аты"))

    class Meta:
        verbose_name = _("Топ")
        verbose_name_plural = _("Топтор")

class Teacher(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Мугалимдин аты"))

    class Meta:
        verbose_name = _("Мугалим")
        verbose_name_plural = _("Мугалимдер")

class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Сабактын аты"))

    class Meta:
        verbose_name = _("Сабак")
        verbose_name_plural = _("Сабактар")

class ScheduleCell(models.Model):
    day = models.CharField(max_length=20, verbose_name=_("Күн"))
    period = models.IntegerField(verbose_name=_("Саат"))
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name=_("Топ"))
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name=_("Сабак"))
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name=_("Мугалим"))
    time = models.TimeField(verbose_name=_("Убакыт"))

    class Meta:
        verbose_name = _("Расписание")
        verbose_name_plural = _("Расписаниелер")
