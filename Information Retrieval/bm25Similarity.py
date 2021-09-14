from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch



es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


queryTitle = input ("Please type a movie title to search: ")
query = {
"match": {"title" : queryTitle}
}

result = es.search(index="movies", body={"query":query})


print("Number of Results: ",len(result['hits']['hits']))


for x in range(len(result['hits']['hits'])):
    print("Movie Title:",result['hits']['hits'][x]['_source']['title'],"Similarity Score: ",result['hits']['hits'][x]['_score'])
    