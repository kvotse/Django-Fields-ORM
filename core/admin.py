from django.contrib import admin
from core import models


admin.site.register(models.Animal)
admin.site.register(models.Plant)
admin.site.register(models.Insects)
admin.site.register(models.Staff)