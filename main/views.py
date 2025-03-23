from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import UserInfo
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# imports for api calls utilizing http, getting json returned from api
from requests import request as rq
from json import loads

def index_view(request):
    # this is sending a request to the database
    user_info = UserInfo.objects.all()

    # make context to use in template:
    my_context = {
        'user_info': user_info,
    }
    # render the 'index.html' template and give it a context in the form of a dictionary
    return render(request, 'index.html', my_context)

'''
def add_view(request):
    my_context = {
    }
    return render(request, 'add.html', my_context)
'''

class add_view(CreateView):
    model = UserInfo
    template_name = 'add.html'
    fields = ['assignment_name', 'due_date']
    success_url = reverse_lazy("index")


def generate_view(request):
    my_context = {}

    # url for api call
    my_url = "https://api.thecatapi.com/v1/images/search?size=med&mime_types=jpg&format=json&has_breeds=true&order=RANDOM&page=0&limit=1"
    # api call
    response = rq("GET", my_url)
    # turn json into Python list
    response_list = loads(response.content)
    # add stuff from api to the context
    my_context["pic_url"] = response_list[0]["url"]

    return render(request, 'generate.html', my_context)

'''
def home_page_view(request):
    # this is sending a request to the database
    img_urls = ImageData.objects.all()

    # make context to use in template:
    my_context = {'img_urls': img_urls}

    # url for api call
    my_url = "https://api.thecatapi.com/v1/images/search?size=med&mime_types=jpg&format=json&has_breeds=true&order=RANDOM&page=0&limit=1"
    # api call
    response = rq("GET", my_url)
    # turn json into dict
    response_list = loads(response.content)
    # add stuff from api to the context
    my_context["pic_url"] = response_list[0]["url"]

    # render the 'home.html' template and give it a context in the form of a dictionary
    return render(request, 'home.html', my_context)


def add_img_url(request):
    cat_img_url = request.GET.get("urlhere")
    ImageData.objects.create(url=cat_img_url)

    # the following is the same as the other view:
    # this is sending a request to the database
    img_urls = ImageData.objects.all()

    # make context to use in template:
    my_context = {'img_urls': img_urls}

    # url for api call
    my_url = "https://api.thecatapi.com/v1/images/search?size=med&mime_types=jpg&format=json&has_breeds=true&order=RANDOM&page=0&limit=1"
    # api call
    response = rq("GET", my_url)
    # turn json into dict
    response_list = loads(response.content)
    # add stuff from api to the context
    my_context["pic_url"] = response_list[0]["url"]

    # render the 'home.html' template and give it a context in the form of a dictionary
    return render(request, 'home.html', my_context)
    '''