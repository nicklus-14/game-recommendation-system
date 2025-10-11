# **Content-Based Game Recommendation System**

# 1.  **Overview**

---

This project utilizes Steam app metadata to recommend games, using Cosine Similarity. The data is comprised of two datasets: [Game Recommendations on Steam](https://www.kaggle.com/datasets/antonkozyriev/game-recommendations-on-steam/) by Anton Kozyriev and the [Steam Games Dataset](https://www.kaggle.com/datasets/fronkongames/steam-games-dataset/) by Martin Bustos.

The game list and numerics are derived from the former dataset, while the game descriptions and categories are sourced from the latter.

# 2. **Usage**

---

To use the recommendation system, follow the steps below:

* Clone repository
* Download [games.csv](https://www.kaggle.com/datasets/antonkozyriev/game-recommendations-on-steam/data?select=games.csv) and [games.json](https://www.kaggle.com/datasets/fronkongames/steam-games-dataset/?select=games.json)     
* Install requirements using ```pip install -r requirements.txt```

Once these prerequisite steps are completed, do the following:

* Run through every cell of ```feature_engineering_and_similarity.ipynb``` until the start of normalization (*there will be a note to mark the stop location*)  
* Write ```streamlit run st_app.py``` within the terminal; this will open the app in your browser
* Use the first box to search for a game, then use the dropdown to select the game
* Choose the amount of recommendation and press the search button
