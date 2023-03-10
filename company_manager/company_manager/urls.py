"""company_manager URL Configuration

PROJEKT URLs
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # http://example.com/admin/3
    path("admin/", admin.site.urls),
]
