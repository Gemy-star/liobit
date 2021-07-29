from main import views
from django.urls import path

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('contact', views.contact_page, name='contact-page'),

]
