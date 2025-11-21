from django.urls import path, include
from django.contrib import admin
from users.views import UsersView, healthcheck

#u<rlpatterns = [
 #   path("users/", UsersView.as_view(), name="users"),
  #  path("healthcheck/", healthcheck, name="healthcheck"),
#]


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("users.urls")),
]
