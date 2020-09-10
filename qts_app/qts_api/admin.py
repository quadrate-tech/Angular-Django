from django.contrib import admin
from .models import payment, ad_type, user, ad_listing, city, district, image, promoted_ad_detail, sub_category

admin.site.register(payment)
admin.site.register(ad_type)
admin.site.register(user)
admin.site.register(ad_listing)
admin.site.register(promoted_ad_detail)
admin.site.register(sub_category)
admin.site.register(image)
