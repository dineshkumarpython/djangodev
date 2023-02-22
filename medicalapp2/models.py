from django.db import models


# Create your models here.
class Num(models.Model):
    Token = models.CharField(max_length=5)


class DocterList(models.Model):
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class DepartmentList(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    appointment_date = models.DateTimeField()
    doctor = models.ForeignKey(DocterList, on_delete=models.CASCADE)
    department = models.ForeignKey(DepartmentList, on_delete=models.CASCADE)
    message = models.CharField(max_length=1100)
    active = models.BooleanField()


class Sample(models.Model):
    name = models.CharField(max_length=230)
    address = models.CharField(max_length=230)
