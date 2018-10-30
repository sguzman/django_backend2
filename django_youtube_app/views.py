from django.http import HttpResponse
import os
import requests
import django_youtube_app
import django_youtube_app.models


host = os.getenv('BHOST', '192.168.1.63')
port = os.getenv('BPORT', '30002')
url = f'http://{host}:{port}/'


def random(request):
    text = requests.get(url).text
    return HttpResponse(text)


# Create your views here.
def index(request, serial, limit):
    print(serial, limit)
    serials = django_youtube_app.models.ChanStats.objects.filter(serial=serial).order_by('-time')[:limit]
    for s in serials:
        print(s.serial, s.time, s.subs)

    return HttpResponse("<h1>Response</h1>")
