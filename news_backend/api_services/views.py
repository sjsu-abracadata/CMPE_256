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
        print(request.data)
        # connect to the mongo client
        client = pymongo.MongoClient(
            'mongodb+srv://dataminingadmin:fall2021project@cluster0.ngjps.mongodb.net/newyorktimes')

        # get the database
        database = client['newyorktimes']

        # get collection weekly_demand
        weekly_demand_collection = database.get_collection("news_articles")
        data = []
        for result in weekly_demand_collection.find()[:10]:
            data.append(
                {
                    "headline": result["article_title"],
                    "body": result["article_summary"],
                    "authors": result["article_authors"],
                    "published_timestamp": result["article_published_date"],
                    "url": result["article_url"],
                    "source": result["source_name"],
                }
            )
        # print(data)
        # total_count = weekly_demand_collection.find().count()
        # record = weekly_demand_collection.find_one()
        return Response(
            data=data,
        )


class CNBCArticlesCountViews(APIView):
    def get(self, request):
        # connect to the mongo client
        client = pymongo.MongoClient('mongodb+srv://dataminingadmin:fall2021project@cluster1.ngjps.mongodb.net/cnbc')

        # get the database
        database = client['cnbc']
        # get collection weekly_demand
        weekly_demand_collection = database.get_collection("news_article")
        data = []
        for result in weekly_demand_collection.find()[:10]:
            data.append(
                {
                    "headline": result["article_title"],
                    "body": result["article_summary"],
                    "authors": result["article_authors"],
                    "published_timestamp": result["article_published_date"],
                    "url": result["article_url"],
                    "source": result["source_name"],
                }
            )
        # print(data)
        # total_count = weekly_demand_collection.find().count()
        # record = weekly_demand_collection.find_one()
        return Response(
            data=data,
            status=status.HTTP_200_OK,
        )

class CNBCArticlesCount(APIView):
    def get(self, request):
        # connect to the mongo client
        client = pymongo.MongoClient('mongodb+srv://dataminingadmin:fall2021project@cluster1.ngjps.mongodb.net/cnbc')

        # get the database
        database = client['cnbc']
        # get collection weekly_demand
        weekly_demand_collection = database.get_collection("news_article")
        # print(data)
        total_count = weekly_demand_collection.find().count()
        record = weekly_demand_collection.find_one()
        return Response(
            data=total_count,
            status=status.HTTP_200_OK,
        )

class NewYorkArticlesCount(APIView):
    def get(self, request):
        # connect to the mongo client
        client = pymongo.MongoClient('mongodb+srv://dataminingadmin:fall2021project@cluster0.ngjps.mongodb.net/newyorktimes')

        # get the database
        database = client['newyorktimes']
        # get collection weekly_demand
        weekly_demand_collection = database.get_collection("news_article")
        # print(data)
        total_count = weekly_demand_collection.find().count()
        record = weekly_demand_collection.find_one()
        return Response(
            data=total_count,
            status=status.HTTP_200_OK,
        )

class SearchAllRecords(APIView):
    def get(self, request, searchparam):
        # connect to the mongo client
        client = pymongo.MongoClient('mongodb+srv://dataminingadmin:fall2021project@cluster0.ngjps.mongodb.net/newyorktimes')
        client1 = pymongo.MongoClient('mongodb+srv://dataminingadmin:fall2021project@cluster1.ngjps.mongodb.net/cnbc')
        # get the database
        database = client['newyorktimes']
        database1 = client1['cnbc']
        # get collection weekly_demand
        weekly_demand_collection = database.get_collection("news_article")
        weekly_demand_collection1 = database1.get_collection("news_article")
        myquery = {"article_title": { "$regex": searchparam }}
        # print(data)
        data = []
        for result in weekly_demand_collection.find(myquery):
            data.append(
                {
                    "headline": result["article_title"],
                    "body": result["article_summary"],
                    "authors": result["article_authors"],
                    "published_timestamp": result["article_published_date"],
                    "url": result["article_url"],
                    "source": result["source_name"],
                }
            )
        for result in weekly_demand_collection1.find(myquery):
            data.append(
                {
                    "headline": result["article_title"],
                    "body": result["article_summary"],
                    "authors": result["article_authors"],
                    "published_timestamp": result["article_published_date"],
                    "url": result["article_url"],
                    "source": result["source_name"],
                }
            )
        return Response(
            data=data,
            status=status.HTTP_200_OK,
        )

        