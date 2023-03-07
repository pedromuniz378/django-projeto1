from django.http import HttpResponse


def home(req):
    return HttpResponse("HOME")


def about(req):
    return HttpResponse("SOBRE")


def contact(req):
    return HttpResponse("CONTATO")
