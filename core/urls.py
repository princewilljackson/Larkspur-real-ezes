from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('advisors/', views.advisors, name='advisors'),
    path('intelligence/', views.intelligence, name='intelligence'),
    path('private-listings', views.private_listings, name='private_listings'),
    path('search/', views.properties_search, name='search'),
    path('services/', views.services, name='services'),
    path('blog/', views.blog, name='blog'),
    path('properties/', views.properties, name='properties'),
    path('property/<slug:slug>/', views.property, name='property'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
    path('about-contact/', views.about_contact, name='about-contact')
]
