import requests
from django.shortcuts import render

def people_home(request):
    # Fetch data from the JSON endpoint using requests library
    response = requests.get('https://dummyjson.com/users')

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        print(data)

        # Pass data to the template for rendering
        return render(request, "people/home.html", {'users': data['users']})
    else:
        # Handle the case when the request was not successful
        return render(request, "error.html", {'error_message': 'Failed to fetch data from the API'})