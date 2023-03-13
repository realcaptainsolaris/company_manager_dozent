# Tag 1: Django

## Virtuelle Umgebungen Grundwissen:
- [Grundwissen virtuelle Umgebungen (en)](https://realpython.com/python-virtual-environments-a-primer/)
- [Virtuelle Umgebungen (de)](https://geekflare.com/de/virtual-environments-python/)

## nachmittag Aufgabe

Ein Projekt eurer Wahl erstellen, zb. ein Wiki.

    git config --global http.proxy http://proxywbs:3128
    git push -u origin main -c http.sslVerify=false
    git push -c http.sslVerify=false -u origin main 
    pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org django
    pip install --proxy=http://proxywbs:3128 -r requirements.txt