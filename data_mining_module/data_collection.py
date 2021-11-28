import logging
import pandas as pd
import yaml
from mongoengine import connect, disconnect
from tqdm import tqdm
import glob
# module imports
from news_articles import parse_article
from database_records import NewsArticles
from utils import check_record_exist


def add_records_to_database(database_config_keys,
                            source_name,
                            article_dataframe):

    # connect to database
    connect(db=database_config_keys['db_name'],
            username=database_config_keys['user_name'],
            password=database_config_keys['password'],
            host=database_config_keys['connection_string'])

    # go through all rows
    for index, row in tqdm(article_dataframe.iterrows(), total=article_dataframe.shape[0]):
        try:
            # check if article already exists
            if not check_record_exist(database_config_keys, row['Article_Link']):
                article_data = parse_article(row['Article_Link'])
                current_article = NewsArticles()
                current_article.source_name = source_name
                current_article.article_title = article_data['article_title']
                current_article.article_authors = article_data['article_authors']

                if len(article_data['article_published_date']) == 0:
                    current_article.article_published_date = row['Date']
                else:
                    current_article.article_published_date = article_data['article_published_date']

                current_article.article_text = article_data['article_text']
                current_article.images_link = article_data['images_link']
                current_article.video_link = article_data['video_link']
                current_article.article_summary = article_data['article_summary']
                current_article.article_keywords = article_data['article_keywords']
                current_article.article_url = article_data['article_url']

                current_article.save()
        except Exception as e:
            logging.error('Failed for article link-' + str(row['Article_Link']))
            logging.error(e)
            print(e)

    disconnect()


if __name__ == '__main__':
    # initializing the logger
    logging.basicConfig(filename='Logs/database_records.log',
                        filemode='w',
                        format='%(name)s - %(levelname)s - %(message)s')

    with open('config.yaml') as f:
        config_dict = yaml.safe_load(f)

    '''
    # list all the files
    nytimes_files = glob.glob(
        "/Users/aryanjadon/Desktop/256_Final_Project/CMPE_256/data_mining_module/data_collection/sitemap/newyork_times/*.xlsx")

    for current_file in nytimes_files:
        try:
            print(current_file)
            current_dataframe = pd.read_excel(current_file)
            add_records_to_database(config_dict['newyork_times_database_details'],
                                    "Newyork Times",
                                    current_dataframe)
        except Exception as e:
            print(e)
    '''

    '''
    cnbc_files = glob.glob(
        "/Users/aryanjadon/Desktop/256_Final_Project/CMPE_256/data_mining_module/data_collection/sitemap/cnbc/*.xlsx")

    for current_file in cnbc_files:
        try:
            print(current_file)
            current_dataframe = pd.read_excel(current_file)
            add_records_to_database(config_dict['cnbc_database_details'],
                                    "CNBC",
                                    current_dataframe)
        except Exception as e:
            print(e)
    '''

