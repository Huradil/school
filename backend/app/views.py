from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.viewsets import ModelViewSet
from .models import School, Teacher, Student, Grade
from .serializers import SchoolSerializer,TeacherSerializer, StudentSerializer, GradeSerializer
from .permissions import IsTeacherOrIsAuthenticated, IsAdminOrReadOnly


class SchoolViewSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    # permission_classes = [IsAdminOrReadOnly]


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = [IsAdminOrReadOnly]


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsTeacherOrIsAuthenticated]


# @receiver(post_save, sender=Student)
# def send_notification_email(sender, instance, created, **kwargs):
#     if created:
#         subject = 'Уведомление о создании ученика'
#         message = f'Ученик {instance.fio} был успешно создан.'
#         from_email = 'nuradiltolokov@gmail.com'
#         to_email = instance.email
#         send_mail(subject, message, from_email, [to_email])


class GradeViewSet(ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [IsTeacherOrIsAuthenticated]



