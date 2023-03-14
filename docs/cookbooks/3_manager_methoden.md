COOKBOOK 4

---------------------------------
Methoden des Managers

Company.objects ist der Manager
---------------------------------

----------------------------------------------------
get  (liefert ein Objekt eines Models)
----------------------------------------------------
company = Company.objects.get(pk=3)
company = Company.objects.get(name="Techno AG", sub_title="We do it")

----------------------------------------------------
all  (liefert alle Objekte eines Models)
----------------------------------------------------
qs = Company.objects.all()

----------------------------------------------------
Slicing
----------------------------------------------------
qs = Company.objects.all()[0:2]

----------------------------------------------------
order_by (eine Queryset-Methode! kann direkt an den Manager angeschlossen werden)
----------------------------------------------------
qs = Company.objects.order_by('name') # aufsteigend
qs = Company.objects.order_by('-name') # absteigend
qs = Company.objects.filter(number_of_employees__gt=3).order_by('-name')


----------------------------------------------------
count() (Anzahl ermitteln)
----------------------------------------------------
number = len(Company.objects.all())  # schlecht
number = Company.objects.count() # gut. Effiziente Methode

----------------------------------------------------
first() (erstes Objekt des Querysets)
----------------------------------------------------
company = Company.objects.first()


----------------------------------------------------
last() (letzetes Objekt des Querysets)
----------------------------------------------------
company = Company.objects.last()
