import pandas as pd
from sklearn.decomposition import TruncatedSVD
import scipy 
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from pandas.api.types import CategoricalDtype
import json

anime_table = pd.read_csv('anime.csv')
rating_table = pd.read_csv('rating.csv')
print ('- Read CSV Data')

rating_table.rating.replace({-1: 0}, regex=True, inplace = True)
print (len(rating_table.anime_id.unique()))
merged = rating_table.merge(anime_table, left_on = 'anime_id', right_on = 'anime_id', suffixes= ['_user', ''])
merged.rename(columns = {'rating_user': 'user_rating'}, inplace=True)
print ('- Merged Data Tables')

users = list(sorted(merged.user_id.unique()))
anime = list(sorted(merged.anime_id.unique()))

with open('anime_ids.json', 'w') as handle:
    json.dump([int(i) for i in anime], handle)
data = merged.user_rating.tolist()

row = merged.user_id.astype(CategoricalDtype(categories=users)).cat.codes
col = merged.anime_id.astype(CategoricalDtype(categories=anime)).cat.codes
R = scipy.sparse.csr_matrix((data, (row, col)), shape=(len(users), len(anime))).T
print ('- Preprocessed Data')
R = TruncatedSVD(100).fit_transform(R)
similarity = cosine_similarity(R)
print ('- Model Built')

def remove(ls, value):
    return list(filter(lambda x: int(x)!= int(value), ls))

top = 10
similar = { int(anime_id): [int(anime[i]) for i in remove(similarity[index].argsort()[::-1].tolist(), anime.index(anime_id))[:top]] for index, anime_id in enumerate(anime) }

with open('similar.json', 'w') as handle:
    json.dump(similar, handle)