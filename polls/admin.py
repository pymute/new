from django.contrib import admin
from .models import StudentModel
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','date_of_birth']
    search_fields=['first_name','last_name']
    
admin.site.register(StudentModel,StudentAdmin)