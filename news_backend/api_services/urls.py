from django.urls import path
from .views import NewYorkArticlesCountViews, CNBCArticlesCountViews

urlpatterns = [
    path('newyorktimes/', NewYorkArticlesCountViews.as_view(), name="newyork_articles_views"),
    path('cnbc/', CNBCArticlesCountViews.as_view(), name="cnbc_articles_views"),
]
