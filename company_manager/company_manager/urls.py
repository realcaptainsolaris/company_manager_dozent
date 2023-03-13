"""company_manager URL Configuration

company_manager/company_manager/urls.py
PROJEKT URLs (Einstiegs URLS)
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # http://example.com/admin/3
    path("admin/", admin.site.urls),

    # http://127.0.0.1:8000/company/hello
    path("company/", include("company.urls")),  # company/urls.py
]
