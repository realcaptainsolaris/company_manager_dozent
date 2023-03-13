""" 
URLs für die APP Company
company_manager/company/urls.py
"""
from django.urls import path
from . import views

app_name = "company"  # ist immer der Name der app

urlpatterns = [
    # http://127.0.0.1:8000/company/hello
    path("hello", views.hello_world, name="hello_world"),
    path("again", views.hello_again, name="hello_again"),
    path("analyze", views.analyze, name="analyze"),
    path("amazon", views.redirect_to_amazon, name="redirect_to_amazon"),

    # http://127.0.0.1:8000/company/world
    path("world", views.redirect_to, name="redirect_to"),
]

"""
fn = views.hello_again
fn(request)

Aufgabe 10 Minuten:
für die URL http://127.0.0.1:8000/company/again
folgende Ausgabe:
hallo again!

python -m venv .envs/companyenv
pip install -r requirements.txt
django-admin startproject company_manager
python manage.py startapp company

"""
