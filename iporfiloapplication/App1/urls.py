from django.urls import path
from App1 import views

urlpatterns = [
    path("",views.home,name="home_page"),
    path("about",views.about,name="about_page"),
    path("resume",views.Resume,name="Resume_page"),
    path("Testimonials",views.Testimonials,name="Testimonials_page"),
    path("contact",views.contact,name="contact_page"),
]