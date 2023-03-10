COOKBOOK zum Erstellen eines neuen Projekts
***********************************************

Diese Anleitung dient zum Erstellen eines Django-Projekts.
Der Konsolen-Befehl "pwd" gibt das aktuelle Arbeitsverzeichnis aus.


falls probleme unter windows:
https://www.com-magazin.de/tipps-tricks/powershell/windows-10-verweigert-ausfuehrung-powershell-skript-2546684.html

----------------------------------------------------------
0.a)  Projektverzeichnis für alle Django-Projekte anlegen
----------------------------------------------------------
mkdir django_projects
cd django_projects


------------------------------------------------------------------
0.b) Verzeichnis für alle virtuellen Environments anlegen
------------------------------------------------------------------
=> Im Verzeichnis .envs wird für jedes Projekt ein eigenes
virtuelles Environment angelegt:

mkdir .envs

falls ein anderes, virtuelles Environment
aktiv sein sollte, dieses jetzt
deaktivieren
---------------------------------
(petenv) deactivate


neues Environment erstellen
---------------------------------
python -m venv .envs/eventenv


virtuelles environment aktivieren:
---------------------------------
.envs\eventenv\Scripts\activate


---------------------------------
1. Projektverzeichnis erstellen
---------------------------------
(eventenv) mkdir event_project

---------------------------------
2. requirements.txt anlegen
---------------------------------
(eventenv) cd  event_project
(eventenv) code .

(Editor öffnet sich, hier jetzt requirements.txt erstellen)
Hier auch eine readme.md erstellen.

---------------------------------
3. Django installieren
---------------------------------
in die requirements.txt die Pakete schreiben

    Django==4.1.3

und auf der Shell installieren:
(eventenv) pip install -r requirements.txt


---------------------------------
4. Projekt erstellen
---------------------------------
(eventenv) pwd
django_projects\event_project
(eventenv) django-admin startproject event_manager

=> Es wird die Dateistruktur angelegt. Nun gibt es ein äußeres
und ein inneres event_manager-Verzeichnis.

(eventenv) cd event_manager

Hinweis: alle zukünftigen Pfadangaben gehen ab jetzt von
event_manager aus.


---------------------------------
5. Settings: Sprache auf deutsch,
Zeitzone (settings.py)
---------------------------------
(eventenv) pwd
event_manager
(eventenv) code .
(Editor öffnet sich)

nun nun müssen wir die
event_manager/event_manager/settings.py
anpassen. Folgende Änderungen vornehmen:

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
LANGUAGE_CODE = 'de-DE'
TIME_ZONE = "Europe/Berlin"
USE_I18N = True
USE_L10N = True
USE_TZ = True

---------------------------------
6. Runserver auf der Shell starten
---------------------------------
(eventenv) pwd
event_manager

(eventenv) python manage.py runserver

prüfen, ob alles OK:
(eventenv) python manage.py check

Website im Browser aufrufen, die Rakete muss fliegen
http://127.0.0.1:8000