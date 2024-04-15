from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError


# Create your models here.

def validate_userid(value):
    if isinstance(value, int):
        raise ValidationError("User ID must be a string.")


class Registermodel(models.Model):
    firstname = models.CharField(max_length=300)
    lastname = models.CharField(max_length=200)
    userid = models.CharField(max_length=100, validators=[validate_userid])
    password = models.IntegerField()
    mblenum = models.BigIntegerField()
    email = models.EmailField(max_length=400, null=True)


class Address_details(models.Model):
    objects = None
    line1 = models.CharField(max_length=300)
    line2 = models.CharField(max_length=300)
    pincode = models.IntegerField()
    state = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    created_by = models.IntegerField(null=False, blank=False)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)


class Contact_details(models.Model):
    objects = None
    mobileno = models.BigIntegerField()
    emailid = models.CharField(max_length=200)
    accountno = models.BigIntegerField()
    beneficaryname = models.CharField(max_length=300)
    created_by = models.IntegerField(null=False, blank=False)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)


class Vendor_details(models.Model):
    objects = None
    vendorname = models.CharField(max_length=300)
    vendorcode = models.CharField(max_length=200)
    vendorgst = models.CharField(max_length=300)
    vendorpan = models.CharField(max_length=300)
    vendorbranch = models.CharField(max_length=300)
    vendoraddress = models.ForeignKey(Address_details, on_delete=models.SET_NULL, null=True)
    vendorcontact = models.ForeignKey(Contact_details, on_delete=models.SET_NULL, null=True)
    created_by = models.IntegerField(null=False, blank=False)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)
