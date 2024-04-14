import genericpath
from django.db import models


#Reddit Class model
class Reddit(models.Model):
    id = models.AutoField(primary_key=True)
    post_id = models.BigIntegerField()
    title = models.TextField()
    date = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['post_id'], name='reddit_postid_uq')
        ]

#Coin Prices model
class CoinPrices(models.Model):
    id = models.AutoField(primary_key=True)
    ticker = models.CharField(max_length=250)
    price = models.FloatField()
    open_price = models.FloatField()
    close_price = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ticker} {self.price}"
    

#Sentiments model
class Sentiments(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    score = models.BooleanField(null=False)
    resource = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text} {self.score}"

#RedditComments model
class RedditComments(models.Model):
    id = models.AutoField(primary_key=True)
    comment_id = models.BigIntegerField()
    post_id = models.ForeignKey(Reddit, on_delete=models.CASCADE)
    text = models.TextField()
    comment_date = models.DateField()
    sentiment_id = models.OneToOneField(Sentiments, on_delete=models.CASCADE, null=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text}"
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['comment_id'], name='reddit_comment_uq')
        ]

#NewsModel
class News(models.Model):
    id = models.AutoField(primary_key=True)
    news_id = models.BigIntegerField()
    title = models.TextField()
    summary = models.TextField()
    sentiment_id = models.OneToOneField(Sentiments, on_delete=models.CASCADE, null=False)
    ticker = models.CharField(max_length=50)
    news_date = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.summary}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['news_id'], name='news_newsid_uq')
        ]


