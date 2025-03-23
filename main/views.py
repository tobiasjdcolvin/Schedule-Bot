from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import UserInfo
from django.views.generic.edit import CreateView, DeleteView, View
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from openai import OpenAI

@login_required
def index_view(request):
    # Only get assignments for the current logged-in user
    user_info = UserInfo.objects.filter(user=request.user)

    my_context = {
        'user_info': user_info,
    }
    return render(request, 'index.html', my_context)


class add_view(LoginRequiredMixin, CreateView):
    model = UserInfo
    template_name = 'add.html'
    fields = ['assignment_name', 'due_date']
    success_url = reverse_lazy("index")
    
    # Override form_valid to set the user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@login_required
def delete_view(request):
    # Only delete the last assignment of the current user
    last = UserInfo.objects.filter(
        user=request.user,
        pk__in=UserInfo.objects.filter(user=request.user).order_by('-id').values('pk')[:1]
    ).delete()
    
    # Get only assignments for the current logged-in user
    user_info = UserInfo.objects.filter(user=request.user)

    my_context = {
        'user_info': user_info,
    }
    return render(request, 'index.html', my_context)


@login_required
def generate_view(request):
    my_context = {}

    f = open("secret_key.txt")
    secretkey = f.read().strip('\n') 

    client = OpenAI(
        api_key=secretkey
    )

    # Only use assignments for the current logged-in user
    prompt = ""
    for info in UserInfo.objects.filter(user=request.user):
        prompt += info.assignment_name + " due by " + str(info.due_date) + ", "

    if(prompt != ""):
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
                Do not use millitary time and use am and pm. \
                leave half hour for breakfast between 8am and 10 am. \
                leave hour for lunch between 12pm and 2pm. \
                leave hour for dinner between 5pm and 8pm."),
            input= prompt,
            temperature=0.2
        )
        my_context["txt_response"] = response.output_text
    else:
        my_context["txt_response"] = "NO ASSIGNMENTS ENTERED"

    return render(request, 'generate.html', my_context)