from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def main (request: HttpRequest) -> HttpResponse:
    return render(request, 'main/base_includes/standart_body_logo.html')
