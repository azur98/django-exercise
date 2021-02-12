from django.http import HttpResponse
from django.views.generic import TemplateView

def helloworld(request):

    return HttpResponse('<h1>hello world</h1>')

class HelloWorldView(TemplateView):
    template_name = 'hello/hello.html'