from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:snake_id>/", views.detail, name="detail"),
    path('accounts/', include('django.contrib.auth.urls')),
]
