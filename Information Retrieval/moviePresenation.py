import imdb

# creating instance of IMDb 
ia = imdb.IMDb() 
#f = open("myfile.txt", "w")



def movieImdbPy(clusterVotes,moviename,clusterVoteAvg):
    # searchning the movie 
    """
    movieId = search[0].movieID
    movie = ia.get_movie('{}'.format(movieId))
    #print(movie.infoset2keys)
    """
    try:
        search = ia.search_movie(moviename)  
        movieId = search[0].movieID
        movie = ia.get_movie('{}'.format(movieId))
        title = movie.get('title')
        plots = movie['plot']
        maxPlot = plots[0]
        for x in plots:
            if len(x) > len(maxPlot):
                maxPlot = x
        movieCast = []
        actors = []
        movieCast.append(movie['cast'][0])
        movieCast.append(movie['cast'][1])
        movieCast.append(movie['cast'][2])
        for x in movieCast:
            actor = x
            actors.append(actor['name'])
        movieYear = movie['year']
        movieCountries = movie['countries']
        movieCountriesString = ', '.join(movieCountries)
        movieDirector = movie['director'][0]['name']
        print("Title: {}".format(title),'       Average clustered user vote average:',clusterVoteAvg,'from a total of',clusterVotes,'votes')
        print("Year: {}".format(movieYear))
        print("Countries: {}".format(movieCountriesString))
        print("Director: {}".format(movieDirector))
        print("Actors: {}, {}, {}".format(actors[0],actors[1],actors[2]))
        print("IMDB Plot:")
        print(maxPlot)
        print("-----------------------------------------------------------")
    except:
        try:
            moviename = moviename[:-6]
            search = ia.search_movie(moviename)
            movieId = search[0].movieID
            movie = ia.get_movie('{}'.format(movieId))
            title = movie.get('title')
            plots = movie['plot']
            maxPlot = plots[0]
            for x in plots:
                if len(x) > len(maxPlot):
                    maxPlot = x
            movieCast = []
            actors = []
            movieCast.append(movie['cast'][0])
            movieCast.append(movie['cast'][1])
            movieCast.append(movie['cast'][2])
            for x in movieCast:
                actor = x
                actors.append(actor['name'])
            movieYear = movie['year']
            movieCountries = movie['countries']
            movieCountriesString = ', '.join(movieCountries)
            movieDirector = movie['director'][0]['name']
            print("Title: {}".format(title),'       Average clustered user vote average:',clusterVoteAvg,'from a total of',clusterVotes,'votes')
            print("Year: {}".format(movieYear))
            print("Countries: {}".format(movieCountriesString))
            print("Director: {}".format(movieDirector))
            print("Actors: {}, {}, {}".format(actors[0],actors[1],actors[2]))
            print("IMDB Plot:")
            print(maxPlot)
            print("-----------------------------------------------------------")
        except:
            #print(moviename,'unsuccessful')
            pass
        """
        print(e)
        print("Title:")
        print("\n")
        print(moviename)
        print("\n")
        print("No data available")
        print("\n")
        print("-----------------------------------------------------------")
        print("")
        print("\n")
        print("No data available for",moviename)
        """

