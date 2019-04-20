# airflow--twitter-restapi--postgresql--demo
Initial tinkering of an airflow process: 
* Read latest tweets based on a chosen hashtag (#captainmarvel)
* Push tweets into a postgresql database

## File structure on airflow after airflow is installed
* AIRFLOW_HOME=~/airflow
* ~/airflow
*     dags
*         Tweet (main business functions)
*             connect.py (connection to database script)
*             data_retrieval.py (getting data)
*         core (execution of business functions)
*             execute_tweets.py (call functions from Tweet)
*         tweets_captain_marvel.py (the dag definition)
