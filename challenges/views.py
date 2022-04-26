from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def index(request):
    return HttpResponse("Index Page")

def monthly_challenges(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = 'January'
    elif month == 'february':
        challenge_text = 'February'
    elif month == 'march':
        challenge_text = 'March'
    else:
        return HttpResponseNotFound("Incorrect month in URL")
    return HttpResponse(challenge_text)
