from django.db import models

# Create your models here.
from django.db import models

class BirthRegistration(models.Model):
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

class DeathRegistration(models.Model):
    full_name = models.CharField(max_length=100)
    date_of_death = models.DateField()
    place_of_death = models.CharField(max_length=100)
    cause_of_death = models.TextField()

    def __str__(self):
        return self.full_name

class MarriageRegistration(models.Model):
    spouse1_name = models.CharField(max_length=100)
    spouse2_name = models.CharField(max_length=100)
    marriage_date = models.DateField()
    place_of_marriage = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.spouse1_name} & {self.spouse2_name}"

class MigrationRegistration(models.Model):
    person_name = models.CharField(max_length=100)
    migration_date = models.DateField()
    from_place = models.CharField(max_length=100)
    to_place = models.CharField(max_length=100)

    def __str__(self):
        return self.person_name

class DivorceRegistration(models.Model):
    spouse1_name = models.CharField(max_length=100)
    spouse2_name = models.CharField(max_length=100)
    divorce_date = models.DateField()
    place_of_divorce = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.spouse1_name} & {self.spouse2_name}"
