from django.contrib import admin
from store.models import Student, Contacts


# Register your models here.

# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'is_active',) # обязательно запятые нужны
    list_filter = ('is_active',) # обязательно запятые нужны
    search_fields = ('first_name', 'second_name',) # для поиска


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'massage',) # обязательно запятые нужны
    list_filter = ('name',) # обязательно запятые нужны
    search_fields = ('name',) # для поиска