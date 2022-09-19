from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from . import views


urlpatterns = [
    path('register/sender/', views.RegisterSenderView.as_view()),
    path('', include('rest_framework.urls')),
    path('register/buyer/', views.RegisterBuyerView.as_view()),
]
