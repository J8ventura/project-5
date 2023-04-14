from django.http import HttpResponse

def index(request):
    print('index')
    homepage = open('static/index.html').read()
    return HttpResponse(homepage)
