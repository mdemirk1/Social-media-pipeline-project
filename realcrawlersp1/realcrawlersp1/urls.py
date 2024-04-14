"""
URL configuration for realcrawlersp1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from realcrawlers_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/subreddit_posts/<search_term>',view=views.get_subreddit_posts),
    path('api/get_alphanews_data',view=views.get_alpha_news_data),
<<<<<<< HEAD
    path('api/get_cyptocurrency/<crypto>', view=views.get_cyrptocurrency),
    path('api/subreddit_comments',view=views.get_subreddit_comments),
=======
    path('api/get_cryptocurrency/<crypto>', view=views.get_cyrptocurrency),
    path('api/subreddit_comments/<search_term>/<post_id>',view=views.get_subreddit_comments)
>>>>>>> 75738b8 (get comments added to views)
]
