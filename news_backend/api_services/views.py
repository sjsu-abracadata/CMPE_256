import pprint
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from mongoengine import connect, disconnect
import glob
import time
import json
import pymongo
import warnings

warnings.filterwarnings('ignore')


# from Backend.data_pipeline.database_tables.database_records import NewsArticle
# News Article View here
class NewYorkArticlesCountViews(APIView):
    def get(self, request):
        # connect to the mongo client
        client = pymongo.MongoClient(
            'mongodb+srv://dataminingadmin:fall2021project@cluster0.ngjps.mongodb.net/newyorktimes')

        # get the database
        database = client['newyorktimes']

        # get collection weekly_demand
        weekly_demand_collection = database.get_collection("news_articles")
        total_count = weekly_demand_collection.find().count()

        record = weekly_demand_collection.find_one()
        return Response({"status": "success",
                         "data": total_count},
                        status=status.HTTP_200_OK)


class CNBCArticlesCountViews(APIView):
    def get(self, request):
        # connect to the mongo client
        client = pymongo.MongoClient('mongodb+srv://dataminingadmin:fall2021project@cluster1.ngjps.mongodb.net/cnbc')

        # get the database
        database = client['cnbc']
        # get collection weekly_demand
        weekly_demand_collection = database.get_collection("news_article")
        total_count = weekly_demand_collection.find().count()
        record = weekly_demand_collection.find_one()
        return Response({"status": "success",
                         "data": {total_count}},
                        status=status.HTTP_200_OK)
