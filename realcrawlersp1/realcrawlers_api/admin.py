from django.contrib import admin
from .models import Reddit
from .models import News
from .models import Sentiments
from .models import RedditComments
from .models import CoinPrices

# Register your models here.

admin.site.register(Reddit)
admin.site.register(News)
admin.site.register(RedditComments)
admin.site.register(CoinPrices)
admin.site.register(Sentiments)