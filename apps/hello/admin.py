from django.contrib import admin
from hello.models import Person, Http_request, Entry

# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    list_display = ('last_name',
                    'name')

admin.site.register(Person, PersonAdmin)
admin.site.register(Http_request)
admin.site.register(Entry)
