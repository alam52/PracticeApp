from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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
    return HttpResponse("Index Page")

def monthy_challenges_num(request, month):
    months = list(monthly_msgs.keys())
    
    try:
        msg_by_num = months[month-1]
    except:
        return HttpResponseNotFound('Incorrect Month Number')
    return HttpResponseRedirect('/challenges/' + msg_by_num)

def monthly_challenges(request, month):

    try:
        challenge_text = monthly_msgs[month]
    except:
        return HttpResponseNotFound('Incorrect month in URL')
    return HttpResponse(challenge_text)
