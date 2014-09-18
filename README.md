stockpredictor
==============

A simple twitter sentiment analysis tool to detect stock market movements.

   demo.rar - It is a streaming api code developed in eclipse platform to gather the tweets about the stocks at particular times.It uses the api version 1.1.

   test.php - It is a REST API code that is developed in php to gather tweets regarding a stock provided its keyword.It uses the api version 1.1.
   
   preprocessing.py  - a python code that is used to remove all the stop words, symbols, etc from the input tweets. It serves to   reduce the noise in the twitter data collected by crawling the api.
   sentiment.py    - a python code that is used to perform effective sentiment analysis on the preprocessed trained tweet sets. Gives an output of the positive and negative tweets
   
   supply:	It contains the folders containing the tweets collected for various stock companies from the twitter api's.
	It also contains the intermediate preprocessed files generated.It contains the sources such as Stopwords.txt, Positive.txt, Negative.txt which are used as dictionaries.
	
