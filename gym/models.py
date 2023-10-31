from django.db import models
from django.contrib.auth.models import User


# Models for the Gym Management System

class Trainer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()
    profile_picture = models.ImageField(upload_to='trainer_profiles/', null=True, blank=True)


class Equipment(models.Model):
    equipment_name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='equipment_images/')


class Category(models.Model):
    category_name = models.CharField(max_length=100)


class PackageType(models.Model):
    type_name = models.CharField(max_length=100)


class Package(models.Model):
    package_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_months = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    package_type = models.ForeignKey(PackageType, on_delete=models.CASCADE)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    booking_date = models.DateField()
    payment_status = models.CharField(max_length=20)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    payment_date = models.DateField(null=True, blank=True)


class Inquiry(models.Model):
    guest_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    inquiry_message = models.TextField()


# Custom User Profile for Registered Users
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    profile_picture = models.ImageField(upload_to='user_profiles/', null=True, blank=True)


# Custom User Profile for Admin
class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='admin_profiles/', null=True, blank=True)


class courses(models.Model):
    # user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    course_name = models.CharField(max_length=55)
    course_desc = models.TextField()
    course_price = models.IntegerField(max_length=10)
    course_img = models.ImageField(upload_to='admin_profiles/', null=True, blank=True)
