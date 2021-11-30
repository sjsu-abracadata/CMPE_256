import logging

import requests
from database_records import ProcessedNewsArticle,NewsArticles
from collections import Counter
from mongoengine import connect, disconnect
import yaml

url = "http://9629-35-201-145-88.ngrok.io/api/analyze"


def process_records_api(database_connection_params):
    """
    function to process database records

    :param database_connection_params: database connection strings
    """

    # connect to database connection through mongoengine
    connect(db=database_connection_params['db_name'],
            username=database_connection_params['user_name'],
            password=database_connection_params['password'],
            host=database_connection_params['connection_string'])

    for document in NewsArticles.objects[100:500]:
        # if not document.overall_article_keywords:
        try:
            print(document['article_url'])
            logging.debug(document['article_url'])
            current_document = ProcessedNewsArticle.objects(cleaned_article_url=document['article_url']).first()
            payload = {'analyze_text': document['article_text']}
            files = []
            headers = {}
            response = requests.request("POST", url, headers=headers, data=payload, files=files)
            current_document.transformers_sentiment = response.json()
            current_document.save()
        except Exception as e:
            print(e)

    # disconnect with the database
    disconnect()


if __name__ == '__main__':
    with open('config.yaml') as f:
        config_dict = yaml.safe_load(f)

        # initializing the logger
    logging.basicConfig(filename='Logs/transformers_api.log',
                        filemode='w',
                        format='%(name)s - %(levelname)s - %(message)s')

    # process_records_api(config_dict['newyork_times_database_details'])
    process_records_api(config_dict['cnbc_database_details'])

