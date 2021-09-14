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
import random
import gensim
from gensim.models import Word2Vec 
from sklearn.cluster import KMeans
from collections import OrderedDict, defaultdict
import warnings
from moviePresenation import *
import warnings
warnings.filterwarnings('ignore')





ratings_data = pd.read_csv("ratings.csv")
movie_names = pd.read_csv("movies.csv")
movie_data = pd.merge(ratings_data, movie_names, on='movieId')
movie_user = movie_data.pivot_table(index='userId',columns='movieId',values='rating')
movieIDsListed = []


trainUserIds = []
validationUserIds = []

def createTrain_ValidationDataframes(df):
    userIDs = ratings_data['userId'].unique().tolist()
    random.shuffle(userIDs)
    validationThreshold = int(len(userIDs)*0.6)
    for x in range(len(userIDs)):
        if x < validationThreshold:
            trainUserIds.append(userIDs[x])
        else:
            validationUserIds.append(userIDs[x])




createTrain_ValidationDataframes(movie_user)

train_ratings = ratings_data[ratings_data['userId'].isin(trainUserIds)]
movie_datatr = pd.merge(train_ratings, movie_names, on='movieId')
train_df = movie_datatr.pivot_table(index='userId',columns='movieId',values='rating')

validation_ratings = ratings_data[ratings_data['userId'].isin(validationUserIds)]
movie_datavl = pd.merge(validation_ratings, movie_names, on='movieId')
validation_df = movie_datavl.pivot_table(index='userId',columns='movieId',values='rating')


globalUserId = int((float(input('Please Type UserID: '))))

movieName_user = movie_data.pivot_table(index='userId',columns='title',values='rating')
userSelection = movieName_user.loc[globalUserId]
#userSelection.index
positiveRatings = pd.Series([])
negativeRatings = pd.Series([])
positiveRatings.columns = ['title', 'rating']

userSelection = pd.DataFrame(userSelection).reset_index()
userSelection.columns = ['title', 'rating']

positiveRatingslist = []
negativeRatingsList = []

for x in range(len(userSelection)):
    if userSelection['rating'][x] >3.4:
        positiveRatingslist.append(userSelection['title'][x])
    elif userSelection['rating'][x]<3.5 and userSelection['rating'][x]>0.1:
        negativeRatingsList.append(userSelection['title'][x])



