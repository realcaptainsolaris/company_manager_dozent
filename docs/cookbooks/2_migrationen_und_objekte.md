
COOKBOOK 3

---------------------------------
Wichtige Befehle mit manage.py
---------------------------------
0. python manage.py runserver
=> den Entwicklungsserver starten und Website unter 127.0.0.1:8000 besuchen

---------------------------------
1. python manage.py makemigrations
=> für alle Apps im Projekt die Migrationsdateien erstellen, falls Änderungen
in den Models gefunden wurden

---------------------------------
2. python manage.py makemigrations pets
=> für die App "pets" die Migrationsdateien erstellen, falls Änderungen
in den Models der App gefunden wurden

---------------------------------
3. python manage.py migrate
=> für alle Apps im Projekt die Datenbank - Migrationen durchführen

---------------------------------
4. python manage.py migrate pets
=> für die Apps "pets" die Datenbank - Migrationen durchführen

---------------------------------
5.  python manage.py sqlmigrate pets 0005
=> für App "pets" und der Migrationsdatei 0005_ das erstelle SQL ausgeben

---------------------------------
6. die interaktive Django-Shell öffnen:

python manage.py shell
>> from pets.models import Pet
>> from company.models import Company

7. Objekt eintragen (INSERT)
---------------------------------
>> p1 = Pet(name="Bambi", age=3)
>> p1.save()

8. Objekt aus DB holen (SELECT)
---------------------------------
>> bambi = Pet.objects.get(pk=1) ODER
>> bambi = Pet.objects.get(name="Bambi")


9. Objekt updaten (INSERT)
---------------------------------
>> bambi = Pet.objects.get(pk=1)
>> bambi.name = "Bamboo"
>> bambi.save()

10. alle Objekt laden
---------------------------------
>> pets = Pet.objects.all()
>> pets[0].name
