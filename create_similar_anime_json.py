import json


similar = json.load(open('similar.json'))
anime = json.load(open('anime.json'))

id_to_anime = {each['anime_id']: each for each in anime }

similar_anime = []
for anime_id, similar_list in similar.items():
    item = id_to_anime[anime_id]
    item['similar'] = similar_list
    similar_anime.append(item)

with open('similar_anime.json', 'w') as handle:
    json.dump(similar_anime, handle)