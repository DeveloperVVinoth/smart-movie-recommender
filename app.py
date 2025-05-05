import streamlit as st
import pickle
import requests

# TMDB API key 
API_KEY = "c4cf1986b9104ad7758a37f50e2bdc74"

# Load model
movies, similarity = pickle.load(open('models/similarity.pkl', 'rb'))

def fetch_poster(movie_title):
    response = requests.get(
        f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_title}"
    )
    data = response.json()
    if data["results"]:
        poster_path = data["results"][0]["poster_path"]
        return f"https://image.tmdb.org/t/p/w500{poster_path}"
    else:
        return ""

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movie_list:
        title = movies.iloc[i[0]].title
        recommended_movies.append(title)
        recommended_posters.append(fetch_poster(title))
    return recommended_movies, recommended_posters

# UI
st.set_page_config(page_title="Smart Movie Recommender", layout="wide")
st.title("🎬 Smart Movie Recommender")

selected_movie = st.selectbox("Choose a movie to get recommendations:", movies['title'].values)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            if posters[i]:
                st.image(posters[i])
            else:
                st.write("🚫 Poster not found")
