import streamlit as st
import pickle

movies_list = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_list['title'].values


st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie:',
    movies_list
)

if st.button('Recommend'):
    st.write('You selected:' , selected_movie_name)
    