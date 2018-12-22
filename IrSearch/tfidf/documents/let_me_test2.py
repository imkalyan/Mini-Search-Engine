import json
with open('/mnt/c/Users/DELL/Desktop/IR/project/movie-json-data-master/json/top-rated-movies-02.json') as json_data:
    d = json.load(json_data)
    for each_detail in d:
        #print(each_detail['genres'])
        tot_genres = ''
        for genres in each_detail['genres']:
            tot_genres = tot_genres + ' ' + genres
        tot_actors = ''
        #print(each_detail['actors'])
        for actor in each_detail['actors']:
            tot_actors = tot_actors + ' ' + actor
        #print(tot_genres)
        #print(tot_actors)

        file_name = each_detail['title'] + '.txt'
        title = each_detail['title']
        year = each_detail['year']
        duration = each_detail['duration']
        releasedate = each_detail['releaseDate'] 
        imdb_rating = each_detail['imdbRating']
        storyline = each_detail['storyline']
        poster_url = each_detail['posterurl']
        
        file_name = each_detail['title'] + '.txt'
        
        f = open(file_name,"w")

        f.write('Title: ' + title  + '\n' + 'Year: ' + str(year) + '\n' + 'genres: ' + tot_genres + '\n' + 'Duration: ' + duration + '\n' + 'ReleaseDate: ' + str(releasedate) + '\n' + 'Storyline: ' + storyline + '\n' + 'Actors: ' + tot_actors + '\n' + 'Imdb Rating: ' + str(imdb_rating) + '\n' + 'Poster url: ' + poster_url)
        f.close
