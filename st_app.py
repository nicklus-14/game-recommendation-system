import streamlit as st
import pandas as pd
st.title('Game Recommendation System')
st.write('This is a simple game recommendation system built with Streamlit.')

df = pd.read_csv('Altered CSVs/merged_game_data.csv')
games = df['title'].tolist()

search_query = st.text_input("Search for a game:")

search_filter = [game for game in games if search_query.lower() in game.lower()]

selected_game = st.selectbox("Select a game:", search_filter)

search_button = st.button("Search")