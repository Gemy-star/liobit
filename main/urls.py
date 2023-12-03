from main import views
from django.urls import path

urlpatterns = [
    path("", views.home_page, name="home-page"),
    path("home", views.home_page, name="home-index"),
    path("maal/versions", views.porjects, name="versions-page"),
    path("about", views.about_page, name="about-page"),
]
