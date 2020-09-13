from django.contrib import admin
from .models import ad_listing, payment
# Register your models here.

admin.site.register(ad_listing)
admin.site.register(payment)
