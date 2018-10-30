from django.http import HttpResponse


# Create your views here.
def index(request, serial, limit):
    print(serial, limit)
    return HttpResponse("<h1>Response</h1>")
