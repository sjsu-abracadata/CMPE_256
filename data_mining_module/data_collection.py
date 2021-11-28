import logging
from mongoengine import connect, disconnect
from tqdm import tqdm

# module imports
from news_articles import parse_article
from database_records import NewsArticles


def add_records_to_database(database_config_keys):
    connect(db='newyorktimes',
            username='dataminingadmin',
            password='fall2021project',
            host='mongodb+srv://dataminingadmin:fall2021project@cluster0.ngjps.mongodb.net/newyorktimes')

    '''
    for index, row in tqdm(newyork_times_file.iterrows(), total=newyork_times_file.shape[0]):
        try:
            article_data = parse_article(row['Article_Link'])
            current_article = NewsArticle()
            current_article.source_name = "Newyork Times"
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
    '''

    disconnect()


if __name__ == '__main__':
    # initializing the logger
    logging.basicConfig(filename='Logs/database_logs.log',
                        filemode='w',
                        format='%(name)s - %(levelname)s - %(message)s')
