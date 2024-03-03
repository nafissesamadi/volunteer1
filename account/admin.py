from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Province)
admin.site.register(models.City)
admin.site.register(models.Job)
admin.site.register(models.UserType)
admin.site.register(models.User)
admin.site.register(models.Profile)
admin.site.register(models.PublicPlace)
