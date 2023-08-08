from rest_framework import serializers
from .models import StudentModel

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentModel
        fields = ('first_name','last_name','phone','email','date_of_birth')
