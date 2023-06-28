from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class School(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Teacher(AbstractUser):
    phone_number = models.CharField(max_length=12,unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='teachers')
    subject = models.CharField(max_length=50)

    groups = models.ManyToManyField(Group, related_name='users', blank=True)
    user_groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='users', blank=True)
    user_set = None

    USERNAME_FIELD = 'phone_number'

    def __str__(self):
        return self.username


class Grade(models.Model):
    name = models.CharField(max_length=50)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='grades')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    fio = models.CharField(max_length=100)
    email = models.EmailField()
    birth_date = models.DateField()
    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True, blank=True)
    male = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.CharField(max_length=100)
    photo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.fio
