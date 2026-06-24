import streamlit as st
import pickle
import pandas as pd
import requests

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

API_KEY = '4b10f82ed49454702abdc7965abc2acb'

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    return f"https://image.tmdb.org/t/p/w500{poster_path}"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies, recommended_posters

movies = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies['title'].values

movies['tags'] = movies['tags'].astype(str)

cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()
similarity = cosine_similarity(vectors)


st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie:',
    movies_list
)

if st.button('Recommend'):
    recommended_movies, recommended_posters = recommend(selected_movie_name)
    for movie, poster in zip(recommended_movies, recommended_posters):
        st.write(movie)
        st.image(poster)
        
        
        