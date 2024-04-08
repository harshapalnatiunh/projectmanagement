import requests
from django.shortcuts import render
from django.http import JsonResponse


    

def people_home(request):
    return render(request,"people/home.html")

def fetch_people_data(request):
    response = requests.get('https://dummyjson.com/users')
    print(response)
    if response.status_code == 200:
        data = response.json()
        return JsonResponse({'users': data['users']})
    else:
        return JsonResponse({'error': 'Failed to fetch data from the API'}, status=500)