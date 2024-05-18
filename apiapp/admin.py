from django.contrib import admin
from .models import Student
# Register your models here.
admin.site.site_header = 'Nishan API'
admin.site.site_title = 'Data of API'
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    field_display = ['id','name','roll','address']