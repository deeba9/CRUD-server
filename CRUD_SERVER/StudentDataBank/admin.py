from django.contrib import admin

# Register your models here.

from .models import Student,Score,User

admin.site.register(Student)
admin.site.register(Score)
admin.site.register(User)
