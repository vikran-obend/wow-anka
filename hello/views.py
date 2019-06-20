from django.shortcuts import render
from django.http import HttpResponse

from .models import Upcoming,News



# Create your views here.
def index(request):

    n = News.objects.all()

    position= 'data-target="#carouselExampleIndicators" data-slide-to="{}"'

    news_data=[]
    for num in n:
        news={
            'pos': position.format(num.news_number),
            'content': num.news_event,
            'class': num.news_class
        }
        news_data.append(news)


    
    print(news_data)
    u = Upcoming.objects.all()

    event_data=[]

    for i in u:
        events={
            'month': i.month,
            'location': i.location,
            'year': i.year,
            'event': i.event       
            }

        event_data.append(events)

    context={
        'event_data':event_data,
        'news_data':news_data
    }
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html", context)



def about(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "about.html")

def recent(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "recent.html")


def support(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "support.html")

def contact(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "contact.html")