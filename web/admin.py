from django.contrib import admin
from .models import Students

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ("st_id", "fname", "lname")


admin.site.register(Students, StudentAdmin)
