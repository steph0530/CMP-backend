import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import TimeStampModel


class Clinic(TimeStampModel):
    clinic_name = models.CharField(max_length=255)

class Department(TimeStampModel):
    name = models.CharField(max_length=255)

class Role(TimeStampModel):
    name = models.CharField(max_length=255)
    department_name = models.ForeignKey(Department, on_delete=models.DO_NOTHING)

class User(AbstractUser):
    uuid = models.UUIDField(
        primary_key=False, default=uuid.uuid4, editable=False
    )
    staff_id = models.CharField(max_length=255)
    clinic = models.ForeignKey(Clinic, on_delete=models.DO_NOTHING)
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.DO_NOTHING)
    role = models.ForeignKey(Role, null=True, blank=True, on_delete=models.DO_NOTHING)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    zodiac = models.CharField(max_length=255, null=True, blank=True)
    staff_code = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, null=True, blank=True)
    resigned_at = models.DateTimeField(null=True, blank=True)
    nickname = models.CharField(max_length=255, null=True, blank=True)
    trail_till = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    color = models.CharField(max_length=255, null=True, blank=True)
    salary_type = models.CharField(max_length=255, null=True, blank=True)
    salary_amount = models.IntegerField(null=True, blank=True)
    have_OT = models.BooleanField(null=True, blank=True)
    rate_OT = models.IntegerField(null=True, blank=True)
    annualLeave = models.IntegerField(null=True, blank=True)

    @property
    def password_set(self):
        if self.password:
            return True
        return False
