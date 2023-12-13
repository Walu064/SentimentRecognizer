import nltk
from nltk.corpus import movie_reviews
import pandas as pd

def generate_learn_data():
    nltk.download('movie_reviews')

    reviews = []
    sentiments = []

    for fileid in movie_reviews.fileids():
        if fileid.startswith('pos'):
            reviews.append(movie_reviews.raw(fileid))
            sentiments.append('positive')
        else:
            reviews.append(movie_reviews.raw(fileid))
            sentiments.append('negative')

    df = pd.DataFrame({
        'review': reviews,
        'sentiment': sentiments
    })

    df.to_csv('reviews.csv', index=False)

if __name__ == "__main__":
    generate_learn_data()