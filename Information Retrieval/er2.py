import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import pairwise_distances
from sklearn import preprocessing
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from progress.bar import FillingSquaresBar
import time

ratings_data = pd.read_csv("ratings.csv")
movie_names = pd.read_csv("movies.csv")
movie_data = pd.merge(ratings_data, movie_names, on='movieId')
movie_user = movie_data.pivot_table(index='userId',columns='title',values='rating')

def findMovieId(movieName):
    for x in range(len(movie_names['title'])):
        if movieName == movie_names['title'][x]:
            movieID = movie_names['movieId'][x]
    return movieID

def findUserVote(userID,movieName):
    movieID = findMovieId(movieName)
    userVote = None
    for x in range(len(ratings_data['rating'])):
        if ratings_data['userId'][x] == userID and ratings_data['movieId'][x] == movieID:
            userVote = ratings_data['rating'][x]
    return userVote

def findMovieAverage(movieName):
    movieID = findMovieId(movieName)
    movieRatingCounter = 0
    totalRatingQ = 0
    for x in range(len(ratings_data['rating'])):
        if ratings_data['movieId'][x] == movieID:
            movieRatingCounter = movieRatingCounter + 1
            totalRatingQ = totalRatingQ + ratings_data['rating'][x]
    movieAverageRating = totalRatingQ/movieRatingCounter
    return format(movieAverageRating,'.3f')

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


queryTitle = input ("Please type a movie title to search: ")
userNumber = int(input("Please type user's ID to search: "))
query = {
"match": {"title" : queryTitle}
}

result = es.search(index="movies", body={"query":query})

movieTitleList = []
similarityScoreList = []
userRatingList = []
movieAverageList = []

print("Number of Results: ",len(result['hits']['hits']))

bar2 = FillingSquaresBar("Fetching Movies", max=len(result['hits']['hits']))

for x in range(len(result['hits']['hits'])):
    #print("Movie Title:",result['hits']['hits'][x]['_source']['title'],"Similarity Score: ",result['hits']['hits'][x]['_score'])
    movieTitle = result['hits']['hits'][x]['_source']['title']
    movieTitleList.append(result['hits']['hits'][x]['_source']['title'])
    similarityScoreList.append(format(result['hits']['hits'][x]['_score'],'.3f'))
    userRatingList.append(findUserVote(userNumber,movieTitle))
    movieAverageList.append(findMovieAverage(movieTitle))
    bar2.next()

print("")
for x in range(len(movieTitleList)):
    time.sleep(.500)
    print("-----------------------------------------------")
    print("Movie Title: ",movieTitleList[x])
    print("BM 25 Similarity Score: ",similarityScoreList[x])
    if userRatingList[x] is not None:
        print("User ID {} Rating: ".format(userNumber),userRatingList[x])
    else:
        pass
    print("Average Movie Rating: ",movieAverageList[x])
    
print("-----------------------------------------------")
