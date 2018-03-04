import pandas as pd
from  elasticsearch import Elasticsearch


train_data_path = '/Users/mbhekne/Desktop/ExploreInnov/Data/train_loan.csv'
test_data_path = '/Users/mbhekne/Desktop/ExploreInnov/Data/test_loan.csv'
train = pd.read_csv(train_data_path)
print(train.shape)
test = pd.read_csv(test_data_path)
print(test.shape)

print "Hi"

from time import time
#from pyelasticsearch import ElasticSearch

CHUNKSIZE=100

index_name_train = "loan_prediction_train"
doc_type_train = "av-lp_train"

index_name_test = "loan_prediction_test"
doc_type_test = "av-lp_test"



def index_data(data_path, chunksize, index_name, doc_type):
    f = open(data_path)
    csvfile = pd.read_csv(f, iterator=True, chunksize=chunksize)
    es = Elasticsearch('http://localhost:9200/')
    es.create(index_name,doc_type,chunksize,id=None)
    try:
        es.delete(index_name,id=None)
    except:
        pass
    es.create(index_name,id=None)
    for i , df in enumerate(csvfile):
        records=df.where(pd.notnull(df), None).T.to_dict()
        list_records=[records[it] for it in records]
        try :
            es.bulk(index_name, doc_type, list_records,id=None)
        except:
            print("error!, skiping chunk!")
            pass

# Indexing train data
index_data(train_data_path, CHUNKSIZE, index_name_train, doc_type_train)



# Indexing test data
#index_data(test_data_path, CHUNKSIZE, index_name_test, doc_type_test)

