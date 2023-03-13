from django.shortcuts import render, redirect
from django.http import HttpResponse


def redirect_to_amazon(request) -> HttpResponse:
    """Leitet die Anfrage an amazon.com weiter.
    http://127.0.0.1:8000/company/amazon
    """
    return redirect("https://amazon.com")


def redirect_to(request) -> HttpResponse:
    """leite weiter auf hello_world."""
    return redirect("/company/hello")


def hello_world(request) -> HttpResponse:
    """Diese View gibt den String Hello World an den Client zurück.

    http://127.0.0.1:8000/company/hello
    """
    return HttpResponse("hallo Welt")


def hello_again(request) -> HttpResponse:
    """Diese View gibt den String Hello Again an den Client zurück.

    http://127.0.0.1:8000/company/again
    """
    return HttpResponse("hallo again")


def analyze(request) -> HttpResponse:
    """
    Analyze the request object.

    http://127.0.0.1:8000/company/analyze
    """
    # print(dir(request))  # was passiert hier?
    print(f"der aktuelle User: {request.user}")
    print(f"die aktuelle HTTP-Methode: {request.method}")
    print(f"die Request Headers: {request.headers}")
    print(f"Folgende Cookies: {request.COOKIES}")
    return HttpResponse("analyze wurde durchgeführt.")
