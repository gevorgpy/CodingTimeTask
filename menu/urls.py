from django.urls import path
from .views import  HomeTextAndTitle

urlpatterns = [
    path('food/', HomeTextAndTitle.as_view()),
]