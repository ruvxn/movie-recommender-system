import pandas as pd 


df = pd.read_csv('datasets/rating.csv')

# Dropping the timestamp column as it is not used 
df = df.drop(columns=['timestamp'])

print(df.head())

#find out how many unique users and movies are in the dataset

num_users = df['userId'].nunique()
num_movies = df['movieId'].nunique()

print(f'number of unique usewr ids: {num_users}')
print(f"number of unique movie ids: {num_movies}")

# user ids rename from 0 - (N-1)
df['userId'] = df['userId'] - 1

#unique movie ids
unique_movie_ids = set(df['movieId'])

#debugging  WARNING - prints out all the unique movie ids
#print(f' unique movie ids : {unique_movie_ids}')

#create a mapping from movie ids 
new_movie_id = {}
count = 0
for movie_id in unique_movie_ids:
    new_movie_id[movie_id] = count
    count += 1

#add the new movie ids to the dataframe
df['movie_idx'] = df.apply(lambda row: new_movie_id[row.movieId], axis=1)

#save the new dataframe to a csv file
df.to_csv('datasets/rating_preprocessed.csv')

