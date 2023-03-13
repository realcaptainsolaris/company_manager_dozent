---------------------------------
7. App erstellen
---------------------------------
(eventenv) pwd
event_manager

(eventenv) python manage.py startapp events

und in den settings registrieren:
event_manager/event_manager/settings.py

MY_APPS = ["events"]
INSTALLED_APPS.extend(MY_APPS)

---------------------------------
8. URLs anlegen
---------------------------------

---------------------------------
a) Die App-URLS in den Projekt-URLs anlegen
---------------------------------
Unter event_manager/event_manager/urls.py

from django.urls import path, include

urlpatterns = [
    path("admin/", include("admin.urls"))
    path("events/", include("events.urls")), <= HIER eintragen!
]

---------------------------------
b) Die App URLs anlegen
---------------------------------
Unter event_manager/events/urls.py

from django.urls import path
from . import views

urlpatterns = [
	path('hello/', views.hello, name='hello'),
]

Der Pfad verweist auf eine nicht existente View hello.
Diese müssen wir noch anlegen.

---------------------------------
9. VIEWS anlegen
---------------------------------
in der App events legen wir jetzt die erste View an:
Unter event_manager/events/views.py

from django.http import HttpResponse

def hello(request):
    return HttpResponse('hello!')


---------------------------------
10. RUNSERVER starten und View testen
---------------------------------
http://127.0.0.1:8000/events/hello