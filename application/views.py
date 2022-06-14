from django.shortcuts import render



import http.client
import json
from .api import api_key
conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': api_key,
    'X-RapidAPI-Host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

conn.request("GET", "/api/npm-covid-data/", headers=headers)

res = conn.getresponse()
data = res.read()

name=data.decode("utf-8")
conv = json.loads(name)
# for country in conv:
#     print(country)
# Create your views here.

    
def index(request):
     covid=conv

     covid={'covid':covid}

     return render(request,'main/index.html',covid)