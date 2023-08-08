from django.db import models
from datetime import datetime
# Create your models here.

class StudentModel(models.Model):
    first_name = models.CharField(default='',max_length=15)
    last_name = models.CharField(default='',max_length=15)
    phone = models.CharField(max_length=13,default='')
    email = models.EmailField()
    date_of_birth = models.DateField(default=datetime.now)

    def __str__(self) -> str:
        return self.first_name
    
    class Meta:
        db_table = 'student'