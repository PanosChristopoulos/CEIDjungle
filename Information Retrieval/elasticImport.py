import csv
from elasticsearch import helpers, Elasticsearch
import json

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
print(es)


def csv_reader(file_obj, delimiter=','):
    global resultCounter
    resultCounter = 0
    reader = csv.DictReader(file_obj)
    i = 1
    results = []
    for row in reader:
        #print(row)
        es.index(index='movies', doc_type='csv', id=i,
                         body=json.dumps(row))
        i = i + 1

        results.append(row)
        resultCounter = resultCounter + 1

try:
    with open("movies.csv") as f_obj:
        csv_reader(f_obj)
        print("A total of {} movies imported in Elasticsearch".format(resultCounter))
except:
    print("Movie import unsuccessful")
