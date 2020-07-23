from django.shortcuts import render
from django.http import HttpResponse

# it needs to be mapped to a URL --> see urls.py

def helloWorld(request):
    user = request.user
    context = {
        'user': user,
    }
    #pass in the request, use the helloworld.html as a variable, and pass in the context variable, which holds a user dictionary
    return render(request, "helloworld.html", context)

"""
#this is a simple view
def index(request):
    return HttpResponse("Hello, world!")
"""