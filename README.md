# airflow--twitter-restapi--postgresql--demo
Initial tinkering of an airflow process: 
* Read latest tweets based on a chosen hashtag (#captainmarvel)
* Push tweets into a postgresql database

## File structure for dags and additional logic at AIRFLOW_HOME
* AIRFLOW_HOME=~/airflow
<br><br>
> dags <br>
>> Tweet (main business functions) <br>
>>> connect.py (connection to database script) <br>
>>> data_retrieval.py (getting data) <br>

>> core (execution of business functions) <br>
>>> execute_tweets.py (call functions from Tweet) <br>

>> tweets_captain_marvel.py (the dag definition) <br>
