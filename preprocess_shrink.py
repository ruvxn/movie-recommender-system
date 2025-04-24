import pandas as pd 
import numpy as np
import pickle
from collections import Counter

# Load the dataset
df = pd.read_csv('datasets/rating_preprocessed.csv')
print("original dataframe size :", len(df))

#Total number of users(N), total number of movies(M)
N = df.userId.max() + 1
M = df.movieId.max() + 1

user_ids_count = Counter(df['userId'])
movie_ids_count = Counter(df['movieId'])

#number of users and movies to shrink to
n= 10000
m= 2000


# Get the most common user ids and movie ids
user_ids= [u for u,c in user_ids_count.most_common(n)]
movie_ids= [m for m,c in movie_ids_count.most_common(m)]

df_small = df[df['userId'].isin(user_ids) & df['movieId'].isin(movie_ids).copy()] 

new_user_id = {}
i = 0
for old in user_ids:
    new_user_id[old] = i
    i += 1
print ("i:", i)

new_movie_id = {}
j = 0
for old in movie_ids:
    new_movie_id[old] = j
    j += 1
print ("j:", j)

print("Setting new ids")

df_small['userId'] = df_small['userId'].astype(int).map(new_user_id)

df_small['movie_idx'] = df_small['movie_idx'].astype(int).map(new_movie_id)


print("new dataframe size :", len(df_small))

# Save the new dataframe to a csv file
df_small.to_csv('datasets/rating_preprocessed_shrink.csv')