import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import pairwise_distances
from sklearn import preprocessing
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from progress.bar import FillingSquaresBar
import time
from kneed import KneeLocator
from sklearn.cluster import KMeans
from collections import OrderedDict, defaultdict
import warnings
from moviePresenation import *





ratings_data = pd.read_csv("ratings.csv")
movie_names = pd.read_csv("movies.csv")
movie_data = pd.merge(ratings_data, movie_names, on='movieId')
movie_user = movie_data.pivot_table(index='userId',columns='movieId',values='rating')
print(movie_user.head())
movieIDsListed = []

globalUserId = int(input('Please Type UserID: '))

for x in range(len(movie_names['movieId'])):
    movieIDsListed.append((movie_names['movieId'])[x])
warnings.filterwarnings("ignore")
"""
print(movieIDsListed)
print(movie_user)
print(len(movie_user),len(movie_user.iloc[1]))
"""

def findMovieTitle(movieId):
    movieTitle = 'temp'
    for x in range(len(movie_names['title'])):
        if movieId == movie_names['movieId'][x]:
            movieTitle = movie_names['title'][x]
    return movieTitle

def findMovieGenre(movieID):
    for x in range(len(movie_names['title'])):
        if movieID == movie_names['movieId'][x]:
            movieGenresList = []
            movieGenresList.append(movie_names['genres'][x].split("|"))

genresList = []


def findUserVote(userID,movieID):
    userVote = None
    userVote = movie_user[movieID][userID]
    return userVote

def findUserRatedMoviesList(userID):
    userRatedList = []
    for x in range(len(ratings_data)):
        if ratings_data['userId'][x] == userID:
            userRatedList.append(ratings_data['movieId'][x])
    return userRatedList

for x in range(len(movie_names['title'])):
    for y in range(len(movie_names['genres'][x].split("|"))):
        if movie_names['genres'][x].split("|")[y] not in genresList:
            genresList.append(movie_names['genres'][x].split("|")[y])



def findMoviesByGenre(genre):
    moviesListbyGenre = []
    for x in range(len(movie_names['title'])):
        for y in range(len(movie_names['genres'][x].split("|"))):
            if movie_names['genres'][x].split("|")[y] == genre:
                moviesListbyGenre.append(movie_names['movieId'][x])
    return moviesListbyGenre

moviesListByGenre = []
for x in genresList:
    moviesListByGenre.append(findMoviesByGenre(x))
    
def userDataAcc(userID):
    userDataAccList = []
    for x in range(len(moviesListByGenre)):
        userRatingSum = 0
        userRatingSum = 0
        userRatingCounter = 0
        userAverage = 0
        for y in range(len(moviesListByGenre[x])):
            try:
                if findUserVote(userID,moviesListByGenre[x][y]) > 0:
                    userRatingSum = userRatingSum + findUserVote(userID,moviesListByGenre[x][y])
                    userRatingCounter = userRatingCounter + 1
            except:
                pass
        try:
            userAverage = round(userRatingSum / userRatingCounter,3)
            
        except:
            userAverage = 0
        userDataAccList.append(userAverage)
    return userDataAccList

bar2 = FillingSquaresBar("Processing", max=len(movie_user),suffix = "Users Calculated: %(index)d/%(max)d  Estimated Time Remaining: %(eta_td)s ")

userDataList = []
fullDataList = []


for x in range(1, len(movie_user)+1):
    userDataList = userDataAcc(x)
    fullDataList.append(userDataList)
    bar2.next()


print("")
fullDataNumPyArray = np.array(fullDataList)
print('data', fullDataNumPyArray)
userDataFrame = pd.DataFrame(fullDataList,columns = genresList)
userDataFrame.index = np.arange(1,len(userDataFrame)+1)


sse = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(fullDataNumPyArray)
    sse.append(kmeans.inertia_)


plt.style.use("fivethirtyeight")
plt.plot(range(1, 11), sse)
plt.xticks(range(1, 11))
plt.xlabel("Number of Clusters")
plt.ylabel("SSE")
plt.show()

kl = KneeLocator(range(1, 11), sse, curve="convex", direction="decreasing")
print("KL elbow is ",kl.elbow,"so, users will be classified into",kl.elbow,'clusters')

kMeansSpecifiedK = KMeans(n_clusters = kl.elbow)
kMeansSpecifiedK.fit(fullDataNumPyArray)

userDataFrame['Cluster'] = kMeansSpecifiedK.predict(fullDataNumPyArray)
movie_user['Cluster'] = kMeansSpecifiedK.predict(fullDataNumPyArray)
modifiedDF = movie_user
modifiedDF.fillna(0)



def findClusteredAverageNan(dataframe,userID):
    cluster = dataframe['Cluster'][userID]
    similarUsers = []
    resultsList = []
    for x in range(1,len(dataframe)+1):
        if dataframe['Cluster'][x] == cluster:
            similarUsers.append(x)
    dataframe2 = dataframe[dataframe['Cluster'] == cluster]
    tempDf = dataframe2.copy()
    try:
        for movie in movieIDsListed:
            dataframe2[movie].fillna(value=round(dataframe[movie].mean(),3), inplace=True)
    except:
        pass
    dataframe2 = dataframe2.dropna(axis='columns')
    fullMovieListClustered = list(dataframe2.iloc[userID].to_dict(OrderedDict).items())
    tempUserRatedList = findUserRatedMoviesList(userID)
    finalMovieList = []
    for x in range(len(fullMovieListClustered)):
        if fullMovieListClustered[x][0] not in tempUserRatedList and fullMovieListClustered[x][0] != 'Cluster':
            finalMovieList.append(fullMovieListClustered[x])
    finalMovieList.sort(key=lambda tup: tup[1], reverse=True)
    print('A total of ',len(fullMovieListClustered) - len(finalMovieList), 'movies clustered have been already rated by user',userID,'- They have been popped from final movie list')
    tempMovieListSize = len(finalMovieList)
    for x in range(len(finalMovieList)):
        votesCounter = 0
        try:
            for y in range(len(similarUsers)):
                if tempDf[finalMovieList[x][0]][similarUsers[y]] > 0.5:
                    votesCounter = votesCounter + 1                 
            if votesCounter<20: 
                finalMovieList.remove(x)
            else:
                resultsList.append([votesCounter,findMovieTitle(finalMovieList[x][0]),finalMovieList[x][1]])  
        except:
            pass
    print("Suggested movies by users in the same cluster: ")
    for x in range(30):
        try:
            print(resultsList[x])
        except:
            pass
    for x in range(30):
        try:
            movieImdbPy(resultsList[x][0],resultsList[x][1],resultsList[x][2])
        except:
            pass

    

findClusteredAverageNan(modifiedDF,globalUserId)