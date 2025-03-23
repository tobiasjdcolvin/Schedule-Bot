from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import UserInfo

# imports for api calls utilizing http, getting json returned from api
from requests import request as rq
from json import loads

# imports for api calls to openAi
from openai import OpenAI

def index_view(request):
    # this is sending a request to the database
    user_info = UserInfo.objects.all()

    # make context to use in template:
    my_context = {
        'user_info': user_info,
    }
    # render the 'index.html' template and give it a context in the form of a dictionary
    return render(request, 'index.html', my_context)

def add_view(request):
    my_context = {
    }

    return render(request, 'add.html', my_context)

def generate_view(request):
    my_context = {}

    client = OpenAI(
    #TODO DELETE THIS BEFORE PUSH
    api_key=""
    )

    prompt = ""
    for info in UserInfo.objects.all():
        prompt+= info.assignment_name + " due by " + str(info.due_date) + ", "
 
        

    response = client.responses.create(
        model= "gpt-4o-mini",
        instructions=("Given a list of assignments and due dates, \
            give a possible schedule that will allow the user to finish \
            the assignment on time."),
        input= prompt
    )

    # add stuff from api to the context
    my_context["txt_response"] = response.output_text

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