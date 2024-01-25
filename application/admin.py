from django.contrib import admin
from . import models


# Register your models here.

class ApplicationAdmin(admin.ModelAdmin):
    # readonly_fields = ['slug', 'rating']
    prepopulated_fields = {'slug': ['demanded_course']}
    list_display = ['rating', 'demanded_course', 'is_active', 'preferred_style']
    list_filter = ['is_active', 'rating']
    list_editable = ['demanded_course', 'is_active', 'preferred_style']

class CourseAdmin(admin.ModelAdmin):
    # readonly_fields = ['slug', 'rating']
    # prepopulated_fields = {'slug': ['demanded_course']}
    list_display = ['is_active', 'course_name', 'grade', 'major', 'code', 'image']
    list_filter = ['course_name', 'grade','major','code']
    list_editable = ['course_name', 'grade', 'major','code']


admin.site.register(models.Grade)
admin.site.register(models.Major)
admin.site.register(models.CourseName)
admin.site.register(models.EducationalLevel)
admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.WeekDay)
admin.site.register(models.AvailableTime)
admin.site.register(models.SkillType)
admin.site.register(models.Skill)
admin.site.register(models.SchoolType)
admin.site.register(models.School)
admin.site.register(models.VenueType)
admin.site.register(models.ClassVenue)
admin.site.register(models.EducationalVolunteer)
admin.site.register(models.SkilledVolunteer)
admin.site.register(models.Student)
admin.site.register(models.Application, ApplicationAdmin)
admin.site.register(models.AcceptedApplication)
