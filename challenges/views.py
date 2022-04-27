from urllib import response
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_msgs = {
    'january':'First month',
    'february': 'Second month',
    'march': 'Third month',
    'april': 'Fourth month',
    'may': 'Fifth month',
    'june': 'Sixth month',
    'july': 'Seventh month',
    'august': 'Eight month',
    'september': 'Ninth month',
    'october': 'Tenth month',
    'november': 'Eleventh month',
    'december': 'Twelfth month'
    }

# Create your views here.
def index(request):
    list_items = ""
    months = list(monthly_msgs.keys())

    for month in months:
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{month}</a></li>"

    response = f"<ul>{list_items}</ul>"
    return HttpResponse(response)

def monthy_challenges_num(request, month):
    months = list(monthly_msgs.keys())
    
    try:
        msg_by_num = months[month-1]
    except:
        return HttpResponseNotFound('<h1>Incorrect Month Number</h1>')
    redirect_path = reverse("month-challenge", args=[msg_by_num])
    return HttpResponseRedirect('/challenges/' + msg_by_num)

def monthly_challenges(request, month):

    try:
        challenge_text = monthly_msgs[month]
        response_data = f"<h1>{challenge_text}</h1>"
    except:
        return HttpResponseNotFound('<h1>Incorrect month in URL</h1>')
    return HttpResponse(response_data)
