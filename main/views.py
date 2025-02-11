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
        'content': '__________________About us__________________',
        'text_on_page': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse eu nibh eu risus lobortis fringilla sit amet sit amet justo. Nam vulputate hendrerit eros. Suspendisse purus mi, blandit dapibus vehicula at, interdum sit amet justo. Fusce at velit sem. Nullam vestibulum tellus a diam malesuada aliquam. Duis rutrum tortor vel odio malesuada porttitor. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Mauris facilisis sed ligula a hendrerit. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nam at eros sit amet turpis lobortis interdum ut at diam. Sed fringilla tortor quam, ac egestas mi posuere a. Phasellus augue lectus, iaculis quis posuere quis, ultricies in tellus. Donec tellus massa, euismod in iaculis et, dignissim a tellus. Integer convallis rutrum feugiat. Phasellus in tempor justo. Nulla bibendum magna ac sapien."

    }

    return render(request, 'main/about.html', context)

def contacts(request):
    context = {
        'title': 'Contacts Page',
        'content': '__________________Our contacts__________________',
        'text_on_page': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse eu nibh eu risus lobortis fringilla sit amet sit amet justo. Nam vulputate hendrerit eros. Suspendisse purus mi, blandit dapibus vehicula at, interdum sit amet justo. Fusce at velit sem. Nullam vestibulum tellus a diam malesuada aliquam. Duis rutrum tortor vel odio malesuada porttitor. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Mauris facilisis sed ligula a hendrerit. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nam at eros sit amet turpis lobortis interdum ut at diam. Sed fringilla tortor quam, ac egestas mi posuere a. Phasellus augue lectus, iaculis quis posuere quis, ultricies in tellus. Donec tellus massa, euismod in iaculis et, dignissim a tellus. Integer convallis rutrum feugiat. Phasellus in tempor justo. Nulla bibendum magna ac sapien."

    }

    return render(request, 'main/contacts.html', context)

def deliver(request):
    context = {
        'title': 'Deliver Page',
        'content': '__________________Deliver__________________',
        'text_on_page': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse eu nibh eu risus lobortis fringilla sit amet sit amet justo. Nam vulputate hendrerit eros. Suspendisse purus mi, blandit dapibus vehicula at, interdum sit amet justo. Fusce at velit sem. Nullam vestibulum tellus a diam malesuada aliquam. Duis rutrum tortor vel odio malesuada porttitor. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Mauris facilisis sed ligula a hendrerit. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nam at eros sit amet turpis lobortis interdum ut at diam. Sed fringilla tortor quam, ac egestas mi posuere a. Phasellus augue lectus, iaculis quis posuere quis, ultricies in tellus. Donec tellus massa, euismod in iaculis et, dignissim a tellus. Integer convallis rutrum feugiat. Phasellus in tempor justo. Nulla bibendum magna ac sapien."

    }

    return render(request, 'main/deliver.html', context)







