from django.contrib import admin
from . import models

admin.site.register(models.Customer)
admin.site.register(models.Pharmacy)
admin.site.register(models.Medicines)
admin.site.register(models.Purchasing)
admin.site.register(models.Sales)
admin.site.register(models.Reports)