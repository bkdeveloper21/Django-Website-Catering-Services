from django.contrib import admin
from user.models import Customer

# Register your models here.

#admin.site.register(Student)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','mobileno')
 
admin.site.register(Customer,CustomerAdmin)