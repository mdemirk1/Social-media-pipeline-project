from rest_framework import serializers
from .models import News
from .models import CoinPrices
from .models import Reddit
from .models import RedditComments
from .models import Sentiments


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title')
    
# class CoinPricesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CoinPrices
#         fields = ('id', 'ticker','price')

# class SentimentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sentiments
#         fields = ('id', 'text','score')

# class ReditSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Reddit
#         fields = ('id', 'post_id', 'title')

# class RedditCommentsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RedditComments
#         fields = ('id', 'title')