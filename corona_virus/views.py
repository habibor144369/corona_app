from django.shortcuts import render
from .models import API
import  requests

# Create your views here.

def hello(request):
    api = API.objects.all() # direct api object not working so this api object for looping....
    for api in api:
        print("ok")

    data = True
    result = None
    globalSummary = True
    countries = None
    while(data):
        try:
            result = requests.get(api) # this 'api' variable for loop variable, 
            json = result.json()

            globalSummary = json['Global']
            countries = json['Countries']

            data = False
        except:
            data = True
    return render(request , 'index.html' ,
                  {'globalSummary' : globalSummary ,
                   'countries' : countries})
                   