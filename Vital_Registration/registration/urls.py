from django.urls import path
from registration import views
from .views import birth_registration, death_registration, marriage_registration, migration_registration, divorce_registration, success

urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('service',views.service,name='service'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('birth_registration', views.birth_registration, name='birth_registration'),
    path('death_registration', views.death_registration, name='death_registration'),
    path('marriage_registration', views.marriage_registration, name='marriage_registration'),
    path('migration_registration', views.migration_registration, name='migration_registration'),
    path('divorce_registration', views.divorce_registration, name='divorce_registration'),
    path('success', views.success, name='success'),
]
