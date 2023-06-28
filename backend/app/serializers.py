from django.core.validators import RegexValidator
from rest_framework import serializers

from .models import School, Teacher, Grade, Student


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True,
                                     validators=[
                                         RegexValidator(
                                             regex='^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=])[\w@#$%^&+=]{8,}$',
                                             message='пароль должен содержать цифру и спецсимвол и он должен быть не менее 8 символов'
                                         )])

    class Meta:
        model = Teacher
        fields = ['username','phone_number', 'school', 'subject', 'password', 'password2','first_name','last_name']

    def validate(self,attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        if password2 != password:
            raise serializers.ValidationError('пароли не совпадают')
        return attrs

    def create(self, validated_data):
        teacher=Teacher(
            username=validated_data['username'],
            phone_number=validated_data['phone_number'],
            password=validated_data['password'],
            school=validated_data['school'],
            subject=validated_data['subject'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        teacher.set_password(validated_data['password'])
        teacher.save()
        return teacher


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Grade
        fields='__all__'

