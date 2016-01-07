from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

"""
# disabled old index view
def index(request):
    return HttpResponse("Rango says: hey, hello world</br><a href='/rango/about'>About</a>")
"""
def index(request):
    # Contruct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage':"I am bold font from the context"}

    # Retrun a rendered response to send to the client
    # we make use of the shortcut function to make our lives easier
    # Note that the first parameter is the template we wish to use.
    return render(request,'rango/index.html',context_dict)

def about(request):
    return HttpResponse("Rango says: here is the about page.</br><a href='/rango/'>Index</a>")
