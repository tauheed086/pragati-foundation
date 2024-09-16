from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('about/',views.about, name="about" ),
        path('gallery/',views.gallery, name="gallery" ),
        path('gallery/', views.person_gallery, name='person_gallery'),
        path('submit-valunteer',views.submit_valunteer, name="submit-valunteer" ),
        path('contact',views.contact, name="contact" ),
        path('donate/<int:id>',views.donate, name="donate" ),
        path('contactus',views.contactus, name="contactus" ),
        path('history',views.history, name="history" ),
        path('donates',views.donates, name="donates" ),
]
