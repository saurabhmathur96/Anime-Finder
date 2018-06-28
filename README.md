# Anime-Finder

An anime recommendation system. It was developed using Anime Ratings Database from ![here](https://www.kaggle.com/CooperUnion/anime-recommendations-database) which was created using data from ![myanimelist.net](myanimelist.net). 

## Requirements

1. Python 3
2. scikit-learn
3. scipy
4. numpy
5. pandas

## Setup

1. Download and extract the dataset to the same directory as the project.
2. Run `compute_svd.py` as `python3 compute_svd.py` to build an Matrix Decomposition based Anime Similarity model and compute the 10 most similar anime for each anime.
3. Run `create_anime_json.py` to convert `anime.csv` to JSON format such that the anime objects are sorted by rating in decreasing order.
4. Run `create_similar_json.py` to convert the similar anime list to a format containing more detail about each anime.


## Execution

Start an HTTP server in the project directory. A simple way to do so is to run `python3 -m http.server` and to view the app, open `http://localhost:8000`.

