from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("apps.snekbook.urls")),
    path("admin/", admin.site.urls),
    path('accounts/', include('apps.accounts.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
]