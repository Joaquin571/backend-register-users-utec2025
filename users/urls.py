from django.urls import path
from .views import UsersView, healthcheck

urlpatterns = [
    path("users/", UsersView.as_view(), name="users"),     
    path("healthcheck/", healthcheck, name="healthcheck"),  
]

