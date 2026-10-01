from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')

def contacts(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        return HttpResponse('Сообщение отправлено. Спасибо.')
    return render(request, 'contacts.html')
