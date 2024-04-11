from django import forms
from .models import BirthRegistration, DeathRegistration, MarriageRegistration, MigrationRegistration, DivorceRegistration

class BirthRegistrationForm(forms.ModelForm):
    class Meta:
        model = BirthRegistration
        fields = ['full_name', 'date_of_birth', 'place_of_birth', 'mother_name', 'father_name']

class DeathRegistrationForm(forms.ModelForm):
    class Meta:
        model = DeathRegistration
        fields = ['full_name', 'date_of_death', 'place_of_death', 'cause_of_death']

class MarriageRegistrationForm(forms.ModelForm):
    class Meta:
        model = MarriageRegistration
        fields = ['spouse1_name', 'spouse2_name', 'marriage_date', 'place_of_marriage']

class MigrationRegistrationForm(forms.ModelForm):
    class Meta:
        model = MigrationRegistration
        fields = ['person_name', 'migration_date', 'from_place', 'to_place']

class DivorceRegistrationForm(forms.ModelForm):
    class Meta:
        model = DivorceRegistration
        fields = ['spouse1_name', 'spouse2_name', 'divorce_date', 'place_of_divorce']
