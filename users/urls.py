from django.urls import path
from .views import UsersView
from .views import healthcheck

urlpatterns = [
    path("users", UsersView.as_view(), name="users"),  # GET/POST /users
    path("healthcheck", healthcheck),
]

