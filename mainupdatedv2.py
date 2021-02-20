# Libraries for mathematical and other basic operations
import numpy as np
import pandas as pd
from flask import Flask, render_template, request

# Libraries for creating Count Matrix and Similarity Matrix for Content Based Method
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Libraries for Creating CSR Matrix and Importing NN Model 
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

# Library for importing trained model
import pickle

def collab(movie_name):

    pivot_table_matrix=pd.read_csv("moviematfinal.csv")

    # Dropping the default index which we get while reading csv and assigning the title column as index
    pivot_table_matrix.set_index("title",inplace=True) 

    # Checking if movie is in our Database.
    if movie_name not in pivot_table_matrix.index:
        return ("This is a String")

    # Loading the trained model.
    collab_model=pickle.load(open('collabmodel.pkl','rb'))

    # Here,before giving to kneighbors function we locate the given movie in the pivot table, then we take only the values(ratings) from it and reshape it according to csr_matrix.
    distance,indices=collab_model.kneighbors(pivot_table_matrix.loc[movie_name].values.reshape(1,-1), n_neighbors=11)
    
    # Making list for nearest movies.
    nearestmovies=[]
    
    for i in range(len(distance.flatten())):
        if i==0:
            pass
        else:
            nearestmovies.append(pivot_table_matrix.index[indices.flatten()[i]])

    return nearestmovies
# define a function that creates similarity matrix
# if it doesn't exist
def create_sim():
    data = pd.read_csv('movies_final.csv')
    # creating a count matrix
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(data['combined'])
    # creating a similarity score matrix
    sim = cosine_similarity(count_matrix)
    return data,sim


# Defining a function that recommends 10 most similar movies
def rcmd(m):
    m = m.lower()
    # Assigning data and similarity matrix
    data, sim = create_sim()
    # Check if the movie is in our database or not
    if m not in data['title'].unique():
        return('This movie is not in our database.\nPlease check if you spelled it correct.')
    else:
        # Getting the index of the movie in the dataframe
        i = data.loc[data['title']==m].index[0]

        # Fetching the row containing similarity scores of the movie
        # From similarity matrix and enumerate it
        lst = list(enumerate(sim[i]))

        # Sorting this list in decreasing order based on the similarity score
        lst = sorted(lst, key = lambda x:x[1] ,reverse=True)

        # Taking top 10 movie scores
        # Not taking the first index since it is the same movie
        lst = lst[1:11]

        # Making an empty list that will containing all 10 movie recommendations
        l = []
        for i in range(len(lst)):
            a = lst[i][0]
            l.append(data['title'][a])
        return l

app = Flask(__name__)

@app.route("/")
def base():
    return render_template('base.html')

@app.route("/home")
def home():
    return render_template('base.html')

@app.route("/recommend")
def recommend():
    
    # Requesting the entered movie at the home page by the user.
    movie = request.args.get('movie')

    # Calling function for content based filtering
    content = rcmd(movie)

    # Calling function for collaborative filtering
    col=collab(movie)

    movie = movie.upper()
    
    #if conditions for the four types of output
    #1 - If the movie is not present in both the databases and no recommendations can be done.
    if type(content)==type('string') and type(col)==type("string"):
        return render_template('recommend.html',t='s',col='s')
    
    #2 - If the movie is present in both the databases(collaborative and content based),
    # Therefore result shows movies with similar content and which are rated similarly by users. 
    elif type(content)==type([]) and type(col)==type([]):
        return render_template('recommend.html',movie=movie,r=content,n=col,t='l',col='l')

    #3 - Here the movie is present in only content based database.
    # Therefore result shows movies with similar content only. 
    elif type(content)==type([]) and type(col)==type("string"):
        return render_template('recommend.html',movie=movie,r=content,t='l',col='s')
    
    #4 - Here the movie is present in only collaborative database.
    # Therefore result shows movies which are rated similarly by the users.
    else:
        return render_template('recommend.html',movie=movie,n=col,t='s',col='l')




if __name__ == '__main__':
    app.run(debug=True)
