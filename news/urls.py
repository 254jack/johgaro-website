from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news_feed, name='news'),
]
