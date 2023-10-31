from django.contrib import admin
from .models import Trainer, Equipment, Category, PackageType, Package, Booking, Inquiry, UserProfile, AdminProfile, courses

# Register the models with the admin site
admin.site.register(Trainer)
admin.site.register(Equipment)
admin.site.register(Category)
admin.site.register(PackageType)
admin.site.register(Package)
admin.site.register(Booking)
admin.site.register(Inquiry)
admin.site.register(UserProfile)
admin.site.register(AdminProfile)
admin.site.register(courses)
