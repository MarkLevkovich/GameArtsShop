from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from goods.models import Categories





def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'Main Page',
        'content': "",
        'categories': categories

    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'About Page',
        'content': 'About us',
        'text_on_page': "This text about our online shop"

    }

    return render(request, 'main/about.html', context)

def contacts(request):
    context = {
        'title': 'Contacts Page',
        'content': 'Our contacts',
        'text_on_page': "This is our contacts..."

    }

    return render(request, 'main/contacts.html', context)

def deliver(request):
    context = {
        'title': 'Deliver Page',
        'content': 'Deliver',
        'text_on_page': "This is our deliver information..."

    }

    return render(request, 'main/deliver.html', context)







