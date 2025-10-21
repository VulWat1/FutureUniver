from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns  # для мультиязычности
from rest_framework import routers
from schedule.views import GroupViewSet, TeacherViewSet, SubjectViewSet, ScheduleCellViewSet

router = routers.DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'cells', ScheduleCellViewSet)

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # URL для смены языка
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('schedule.urls')),  # фронтенд
)
urlpatterns += router.urls