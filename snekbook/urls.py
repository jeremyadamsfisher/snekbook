from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("profile/<int:user_id>", views.profile, name="profile"),
    path("detail/<int:snake_id>/", views.detail, name="detail"),
    path("unlike/<int:snake_id>/", views.unlike_snake, name="unlike"),
    path("list/<int:cursor>", views.list, name="list"),
    path("accounts/", include("django.contrib.auth.urls")),
]
