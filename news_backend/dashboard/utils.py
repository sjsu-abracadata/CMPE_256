from mongoengine import connect, disconnect
import glob
import json
import pymongo


def calculate_number_of_records(database_connection_string,
                                database_name,
                                collection_name):
    try:
        # connect to the database
        client = pymongo.MongoClient(database_connection_string)

        # get the database
        database = client[database_name]

        # get collection name
        weekly_demand_collection = database.get_collection(collection_name)

        # get the total count
        total_count = weekly_demand_collection.find().count()

        # return total count
        return total_count
    except Exception as e:
        return 0

