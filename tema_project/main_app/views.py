from django.shortcuts import render
import json

def home(request):
    with open('person.json') as f:
        person_info = json.load(f)


    return render (request, 'main_app/home.html', {'person': person_info})