from django.shortcuts import render
import requests

def news_feed(request):
    API_KEY = "pub_8405c9a33e9e4dc59ee6c8285717ce7e"
    url = f"https://newsdata.io/api/1/news?apikey={API_KEY}&category=food&language=en"

    response = requests.get(url)
    data = response.json()
    articles = data.get("results", [])

    return render(request, 'news.html', {'articles': articles})
