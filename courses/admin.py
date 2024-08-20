from django.contrib import admin
from .models import Course, CourseInstance

class CourseInstanceInline(admin.TabularInline):
    model = CourseInstance
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    inlines = [CourseInstanceInline]
    list_display = ('title', 'code', 'description')

admin.site.register(Course, CourseAdmin)