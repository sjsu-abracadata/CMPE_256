import data_preprocessing
from database_records import ProcessedNewsArticle
import pymongo
from mongoengine import connect, disconnect
import yaml


def process_records(database_connection_params):
    """
    function to process database records

    :param database_connection_params: database connection strings
    """

    # connect to database connection through mongoengine
    connect(db=database_connection_params['db_name'],
            username=database_connection_params['user_name'],
            password=database_connection_params['password'],
            host=database_connection_params['connection_string'])

    for document in ProcessedNewsArticle.objects:
        if not document.overall_article_keywords:
            all_keywords = []
            try:
                for words in document['cleaned_article_keywords']:
                    all_keywords.append(words)

                if 'FAC' in document['cleaned_recognized_entity']:
                    temp_list = document['cleaned_recognized_entity']['FAC']
                    all_keywords += temp_list

                if 'GPE' in document['cleaned_recognized_entity']:
                    temp_list = document['cleaned_recognized_entity']['GPE']
                    all_keywords += temp_list

                if 'LOC' in document['cleaned_recognized_entity']:
                    temp_list = document['cleaned_recognized_entity']['LOC']
                    all_keywords += temp_list

                if 'PERSON' in document['cleaned_recognized_entity']:
                    temp_list = document['cleaned_recognized_entity']['PERSON']
                    all_keywords += temp_list

                if 'ORG' in document['cleaned_recognized_entity']:
                    temp_list = document['cleaned_recognized_entity']['ORG']
                    all_keywords += temp_list

                document.overall_article_keywords = list(set(all_keywords))

                document.save()

            except Exception as e:
                print(e)

    # disconnect with the database
    disconnect()


if __name__ == '__main__':
    with open('config.yaml') as f:
        config_dict = yaml.safe_load(f)

    # process_database_records(config_dict['newyork_times_database_details'])
    process_records(config_dict['cnbc_database_details'])


