from django.http import JsonResponse
import os
import django_youtube_app
import django_youtube_app.models


host = os.getenv('BHOST', '192.168.1.63')
port = os.getenv('BPORT', '30002')
url = f'http://{host}:{port}/'
max_limit = 1000


# Create your views here.
def index(request, serial, limit=max_limit):
    print(serial, limit)
    if limit > max_limit:
        limit = max_limit

    serials = django_youtube_app.models.ChanStats.objects.filter(serial=serial).order_by('-time')[:limit]

    json_body = {
        'serials': []
    }
    for s in serials:
        json_body['serials'].append({
            'serial': s.serial,
            'time': s.time,
            'subs': s.subs
        })

    return JsonResponse(json_body)
