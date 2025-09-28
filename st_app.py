import streamlit as st
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MultiLabelBinarizer
mlb = MultiLabelBinarizer()

st.set_page_config(page_title="Game Recommender", layout="centered")
st.title('Game Recommendation System')
st.write('This is a simple game recommendation system built with Streamlit.')

@st.cache_data(show_spinner=True)

def load_data():
    return pd.read_parquet('preprocessed_games.parquet')
df = load_data()

genres_matrix = mlb.fit_transform(df['genres'])

rating_dict = {
    'Overwhelmingly Positive': 9,
    'Very Positive': 8,
    'Positive': 7,
    'Mostly Positive': 6,
    'Mixed': 5,
    'Mostly Negative': 4,
    'Negative': 3,
    'Very Negative': 2,
    'Overwhelmingly Negative': 1
}
df['rating_normalized'] = (df['rating'].map(rating_dict) - 1) / 8

df['positive_ratio_log'] = np.log1p(df['positive_ratio'])
df['price_log'] = np.log1p(df['price_final'])
df['user_reviews_log'] = np.log1p(df['user_reviews'])

embeddings = np.load('embeddings.npy')
tags = genres_matrix
numerics = df[['price_log', 'positive_ratio_log', 'user_reviews_log']].values
X = np.hstack([numerics*0.2, embeddings*0.3, tags*0.5])
cs_matrix = cosine_similarity(X)

def recommend(df, appid, cs_matrix, k=10):
    index = df[df['app_id'] == appid].index[0]
    pos = df.index.get_loc(index)
    scores = cs_matrix[pos].copy()
    scores[pos] = -np.inf
    indexes = np.argsort(scores)[-k:][::-1]
    return df.iloc[indexes]

del embeddings, tags, numerics, X, rating_dict, genres_matrix

games = df['title'].tolist()

search_query = st.text_input("Search for a game:")

search_filter = [game for game in games if search_query.lower() in game.lower()]

selected = st.selectbox("Your favorite", ["(Select a game)"] + search_filter)
k = st.slider("How many recommendations?", 5, 20, 10)

search_button = st.button("Search")

if search_button:
    if not selected or selected == "(Select a game)":
        st.warning("Pick a game first.")
    else:
        appid = df[df['title'] == selected]['app_id'].values[0]
        recommendations = recommend(df, appid, cs_matrix, k=k)
        st.subheader("We recommend:")
        for i, row in recommendations.iterrows():
            st.write(row['title'])