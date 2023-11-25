from django.contrib import admin
from .models import Employee, Face

class MemberAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")
    prepopulated_fields = {"slug": ("first_name", "last_name")}

admin.site.register(Employee, MemberAdmin) 
admin.site.register(Face)