# from django.urls import path
# from django.views.generic import TemplateView

# urlpatterns = [
#     # Главная страница с таблицей расписания
#     path('', TemplateView.as_view(template_name='schedule/index.html'), name='schedule_home'),
# ]

from rest_framework import routers
from django.urls import path, include
from .views import GroupViewSet, TeacherViewSet, SubjectViewSet, ScheduleCellViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'cells', ScheduleCellViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.IndexView.as_view(), name='index'),  # your main page
]
urlpatterns += router.urls