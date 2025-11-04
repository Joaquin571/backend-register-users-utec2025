from django.urls import path
from .views import UsersView, healthcheck

urlpatterns = [
    path("users/", UsersView.as_view(), name="users"),      # GET/POST /users/
    path("healthcheck/", healthcheck, name="healthcheck"),  # GET /healthcheck/
]

