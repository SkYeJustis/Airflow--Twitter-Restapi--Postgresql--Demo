from Tweet.connect import create_engine_pgsql, insert_to_db
from Tweet.data_retrieval import ApiData

def core_get_data(**kwargs):
    task_instance = kwargs['ti']
    tweets_df = ApiData().get_twitter_data_by_hashtag('#captainmarvel', 50)
    task_instance.xcom_push(key='tweets_df', value=tweets_df)


def core_db_insert_to_db(**kwargs):
    task_instance = kwargs['ti']
    engine = create_engine_pgsql()
    tweets_df = task_instance.xcom_pull(key='tweets_df', task_ids='get_data')
    insert_to_db(engine, tweets_df, 'Captain_Marvel_Tweets')