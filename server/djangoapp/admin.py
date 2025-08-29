from django.contrib import admin
from .models import CarMake, CarModel  # related models

# Register your models here.

# CarModelInline class
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # Number of empty forms to display

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year')
    list_filter = ('car_make', 'type', 'year')
    search_fields = ('name',)

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name', 'description')
    search_fields = ('name',)

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
