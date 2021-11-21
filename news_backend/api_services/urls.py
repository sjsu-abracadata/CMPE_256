from django.urls import path
from .views import NewYorkArticlesCountViews, CNBCArticlesCountViews, CNBCArticlesCount, NewYorkArticlesCount, SearchAllRecords

urlpatterns = [
    path('newyorktimes/', NewYorkArticlesCountViews.as_view(), name="newyork_articles_views"),
    path('cnbc/', CNBCArticlesCountViews.as_view(), name="cnbc_articles_views"),
    path('cnbccount/', CNBCArticlesCount.as_view(), name="cnbc_articles_count"),
    path('newyorktimescount/', NewYorkArticlesCount.as_view(), name="ny_articles_count"),
    path('searchallrecords/<searchparam>', SearchAllRecords.as_view(), name="search_all_records")
]
