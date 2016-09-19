from django.contrib import admin
from cars.models import Car

# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ('brand',
                    'model')

admin.site.register(Car, CarAdmin)
