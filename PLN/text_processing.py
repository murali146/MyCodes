import nltk
from  elasticsearch import Elasticsearch
import pandas


#nltk.download()

#from nltk.tokenize import sent_tokenize, word_tokenize

#EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

#print(sent_tokenize(EXAMPLE_TEXT))

#print(word_tokenize(EXAMPLE_TEXT))


es = Elasticsearch()

CHUNKSIZE = 100

index_name_train = "loan_prediction_train"
doc_type_train = "av-lp_train"

index_name_test = "loan_prediction_test"
doc_type_test = "av-lp_test"


