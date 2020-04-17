# Real-Time-Twitter-Sentiment-analysis-using-kafka

Prerequisite requirement:
1. Developer account in twitter( for consumer_key, consumer_secret_key,access_token, access_secret_token).
2. Kafka downloaded and installed.
3. Elastic Search downloaded and installed.
4. Kibana downloaded and installed.
5. Spark downloaded and instaleld.
6. Any IDE for python.

IDE - PyCharm
using python and pyspark

Source file:
Scrapper_KafkaProducer.py : contains the scraper program which collects tweet and filter them according to the hashtags(#trump and #coronavirus here)
SentimentAnalyzer_KafkaConsumer.py : contains the Kafka consumer which takes the data from the producer in json format and it also consists of sentiment analyzer which analyzes the sentiment related to each tweet(from json) and sends it to elastic search for visualization.

For Visualization- Elastic Search and Kibana is used

Steps to execute:
1.Open Terminal Window 1:
    Go to your Kafka directory and run the following
    bin/zookeeper-server-start.sh config/zookeeper.properties
    Keep the terminal window running.

2.Open Terminal Window 2:
    Go to your Kafka directory and run the following
    bin/kafka-server-start.sh config/server.properties
    Keep the terminal window running.

3.Run the Scrapper_KafkaProducer.py program in the IDE.

4.Open another terminal and run the following
  bin/kafka-topics.sh --list --zookeeper localhost:2181
  It will show the topic associated with your program(here: twitter)

5.Open another terminal: Go to elastic search directory then bin and run the following
 chmod 755 elasticsearch
 ./elasticsearch

6.Open another terminal: Go to kibana directory then bin and run the following
 chmod 755 kibana
./kibana

(In kibana elasticsearch host should be set to your elastic search instance)

7.Run the SentimentAnalyzer_KafkaConsumer.py in the IDE.

8.Now the data for visualization has been sent to the kibana portal

9.Open http://localhost:5601 in your browser : this will open kibana

10.Create your index pattern : Your index pattern should match with the one mentioned in your consumer program( Here : Sentiment)

11.Go to Visualization, Select your index pattern, Select the type of visualization such as pie chart or heat map.

12.Select the following options:(for pie chart)

split slices -> 
aggregation : Terms -> 
field : sentiment.keyword -> 
order by: Metric:count ->
order : Descending and size: 5

13. Click play sort of button in the top to create the chart/graph.






