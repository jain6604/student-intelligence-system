from django.contrib import admin
from .models import Student, Lifestyle, Performance


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch', 'program', 'year', 'semester')
    search_fields = ('name', 'branch')
    list_filter = ('program', 'year')


@admin.register(Lifestyle)
class LifestyleAdmin(admin.ModelAdmin):
    list_display = ('student', 'study_hours', 'sleep_hours', 'screen_time', 'attendance')
    list_filter = ('attendance',)


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'cgpa', 'assignments_completed')
    list_filter = ('cgpa',)