# import genericpath
import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import render

from dotenv import load_dotenv
import os

from rest_framework.decorators import api_view
from rest_framework import generics, status
from .serializers import *
from .models import News
from realcrawlers_api import models
from rest_framework import status, generics



# from .serializers import *

load_dotenv()
# Retrieve the Crunchbase API key from the environment variables
alpha_api_key = os.getenv("ALPHAVANTAGE_API_KEY")

alpha_url = "https://www.alphavantage.co/query?"
reddit_baseUrl = 'https://www.reddit.com'

# @api_view(['GET'])
# class NewsListView(genericpath.ListAPIView):
#     model = News
#     serializer_class = NewsSerializer


@api_view(['GET', 'POST'])
# Create your views here.
def get_subreddit_posts(request, search_term):
    try:
        response = requests.get(f'{reddit_baseUrl}/r/{search_term}/hot.json', headers={"User-Agent": "Flask Reddit App"})
        response.raise_for_status()
        data = response.json()
        return JsonResponse(data)

    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': f'Error: {e}'}), 500

def get_alpha_news_data(request):
    parameters = {
        "function": "NEWS_SENTIMENT",
        "tickers": "COIN,CRYPTO:BTC,FOREX:USD",
        "time_from": "20220410T0130",
        "limit": "2",
        "apikey": alpha_api_key
    }
    # print("params",params)

    try:
        response = requests.get(alpha_url, params=parameters)
        
        if response.status_code == 200:
            if response.status_code == 200:
                data = response.json()
                return JsonResponse(data)
            else:
                return JsonResponse({"error": "Failed to retrieve data from Alpha Vantage."}), 500
        else:
            return JsonResponse({"error": "Failed to retrieve data from Alpha Vantage."}), 500
    except Exception as e:
        return JsonResponse({"error": str(e)}), 500
    

def get_cyrptocurrency(request, crypto):
    params = {
        "function": "DIGITAL_CURRENCY_DAILY",
        "symbol": crypto,
        "market": "USD",
        "apikey": alpha_api_key
    }
    try:
        response = requests.get(alpha_url, params=params)
        if response.status_code == 200:
            data = response.json()
            return JsonResponse(data)
        else:
            return JsonResponse({"error": "Failed to retrieve data from Alpha Vantage."}), 500
    except Exception as e:
        return JsonResponse({"error": str(e)}), 500

def get_subreddit_comments(request, search_term, post_id):
    # this is name (id) example t3_175jl1l
    # post_id is just this part 175jl1l
    # search_term is subreddit name
    try:
        response = requests.get(f'{reddit_baseUrl}/r/{search_term}/comments/{post_id}.json', headers={"User-Agent": "Flask Reddit App"})
        response.raise_for_status()
        data = response.json()[1]
        # response.json() is list of two json objects
        # first item describes the post
        # comments are in the second item of list
        # comment texts can be found in response.json()[1] -> data -> children
        # this children is also list of json objects

        # for item in response.json()[1]["data"]["children"]:
        #     print("Comment -->")
        #     print(item["data"]["body"])
        # this for loop above only access comments (their replies are not included)
        
        return JsonResponse(data)

    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': f'Error: {e}'}), 500

def get_subreddit_comments(request):
    parameters = {
        
    }
    # print("params",params)

    # try:
        # response = requests.get(alpha_url, params=parameters)
        
    #     if response.status_code == 200:
    #         if response.status_code == 200:
    #             data = response.json()
    #             return JsonResponse(data)
    #         else:
    #             return JsonResponse({"error": "Failed to retrieve data from Alpha Vantage."}), 500
    #     else:
    #         return JsonResponse({"error": "Failed to retrieve data from Alpha Vantage."}), 500
    # except Exception as e:
    #     return JsonResponse({"error": str(e)}), 500
    return JsonResponse({"data":"test"})


# if __name__ == '__main__':
#     app.run(debug=True)