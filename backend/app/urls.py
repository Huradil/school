from rest_framework import routers
from django.urls import path,include
from .views import SchoolViewSet,TeacherViewSet,StudentViewSet,GradeViewSet
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'schools', SchoolViewSet)
router.register(r'teacher',TeacherViewSet)
router.register(r'student',StudentViewSet)
router.register(r'grade',GradeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/',obtain_auth_token),
    path('auth/',include('rest_framework.urls')),
]