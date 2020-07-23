from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    products = ["Cherries","Apples","Oranges","Strawberries","Pears","Watermelons"]
    context = {
        'products': products, #the key is the string 'products' and the value is the list 'products'
    }
    #pass in the request, use the home.html as a variable, and pass in the context variable, which holds a user dictionary
    return render(request, "home.html", context)