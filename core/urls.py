# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("e-solar/admin/", admin.site.urls),                # Django admin route
    path("e-solar/", include("apps.authentication.urls")),  # Auth routes - login / register
    path("e-solar/", include("apps.home.urls")),            # UI Kits Html files
]