from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('beans/', views.beans, name='beans'),
    path('corns/', views.corns, name='corns'),
    path('peas/', views.peas, name='peas'),
    path('wheat/', views.wheat, name='wheat'),
    path('contact/', views.contact_view, name='contact'),
]
