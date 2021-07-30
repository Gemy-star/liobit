from main import views
from django.urls import path

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('contact', views.contact_page, name='contact-page'),
    path('category/<int:pk>', views.porjects, name='cat-page'),
    path('about', views.about_page, name='about-page'),

]
