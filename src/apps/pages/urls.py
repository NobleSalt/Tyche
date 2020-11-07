from django.urls import path
from .views import (
    Home,
    About,
    Contact,
    Menu,
    Blog
    )

app_name = 'page'

urlpatterns = [
    path("home/", Home.as_view(), name="home"),
    path("about/", About.as_view(), name="about"),
    path("contact/", Contact.as_view(), name="contact"),
    path("menu/", Menu.as_view(), name="menu"),
    path("blog/", Blog.as_view(), name="blog"),
]
