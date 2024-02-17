import streamlit as st
from components.prediction import modelPrediction
from helper import load_pickle,movie_list

new_df = load_pickle("new_df.pkl")
model = load_pickle("model.pkl")

prediction = modelPrediction(new_df,model)
# movies = prediction.recommend("Avatar")

# print(movies)

st.title("Movie Recommender System")

user_movie = st.selectbox(label="Select the movie",placeholder="Chose a movie",options=new_df["title"].values)
modelprediction = modelPrediction(new_df,model)
suggested_movies = modelprediction.recommend(user_movie)

st.write(suggested_movies)