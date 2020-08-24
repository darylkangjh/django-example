from django.shortcuts import render, HttpResponse

# Create your views here.
def welcome(request):
    return render(request, 'books/index.template.html')

def index(request):
    return HttpResponse('Books')