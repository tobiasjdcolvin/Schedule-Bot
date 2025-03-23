from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import UserInfo
from django.views.generic.edit import CreateView, DeleteView, View
from django.urls import reverse_lazy

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


def delete_view(request):
    last = UserInfo.objects.filter(pk__in=UserInfo.objects.order_by('-id').values('pk')[:1]).delete()
    # this is sending a request to the database
    user_info = UserInfo.objects.all()

    # make context to use in template:
    my_context = {
        'user_info': user_info,
    }
    # render the 'index.html' template and give it a context in the form of a dictionary
    return render(request, 'index.html', my_context)

def generate_view(request):
    my_context = {}

    f = open("secret_key.txt")
    secretkey = f.read().strip('\n') 

    client = OpenAI(
    api_key=secretkey
    )

    prompt = ""
    for info in UserInfo.objects.all():
        prompt+= info.assignment_name + " due by " + str(info.due_date) + ", "
 
        

    response = client.responses.create(
        model= "gpt-4o-mini",
        instructions=("Given a list of assignments and due dates, \
            give a possible schedule that will allow the user to finish \
            the assignment on time. The schedule should broken up by days \
            where each day is broken up by hours. \
            Each time the user switches to a new assignment, there is a new line. \
            This is only for assignment lines. \
            Additionally each line involving an assignment will take the form \
            [time1] - [time2]: work on [assignment], where time1 is the \
            starting time, time2 is the ending time, and \
            assignment is the current assignment they're working on.\
            Each line has a limit of 80 characters so keep lines short. \
            Each assignment has a minimum of 1 hour put into it. \
            The earliest time is at 8:00 am and the latest time is be 10:00 pm.\
            Do not use first person or second person.\
            Do not use phases of the day.\
            Prioritize assignments where the nearer the due date, the more important. \
            Don't use mark down format. \
            Add multiple breaks per day, each break is 30 minutes mininum.\
            Do not use millitary time. \
            leave half hour for breakfast between 8am and 10 am. \
            leave hour for lunch between 12pm and 2pm. \
            leave hour for dinner between 5pm and 8pm."),
        input= prompt,
        temperature=0.3
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