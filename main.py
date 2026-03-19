# =========================
# 1. IMPORT LIBRARIES
# =========================
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


# =========================
# 2. LOAD DATA
# =========================
books = pd.read_csv("Books.csv", low_memory=False)
users = pd.read_csv("Users.csv")
ratings = pd.read_csv("Ratings.csv")


# =========================
# 3. DATA CLEANING
# =========================

# Remove books without title
books = books.dropna(subset=['Book-Title'])

# Fill missing values (SAFE way)
books['Book-Author'] = books['Book-Author'].fillna('Unknown')
books['Image-URL-M'] = books['Image-URL-M'].fillna('https://via.placeholder.com/150')

# Remove duplicate ISBNs (better than title)
books = books.drop_duplicates('ISBN')


# =========================
# 4. MERGE DATA
# =========================
ratings_with_name = ratings.merge(books, on="ISBN")


# =========================
# 5. POPULARITY-BASED SYSTEM
# =========================

# Number of ratings
num_rating = ratings_with_name.groupby('Book-Title')['Book-Rating'].count().reset_index()
num_rating.rename(columns={'Book-Rating': 'num_ratings'}, inplace=True)

# Average rating
avg_rating = ratings_with_name.groupby('Book-Title')['Book-Rating'].mean().reset_index()
avg_rating.rename(columns={'Book-Rating': 'avg_ratings'}, inplace=True)

# Merge both
popularity_df = num_rating.merge(avg_rating, on='Book-Title')

# Filter top books
popularity_df = popularity_df[popularity_df['num_ratings'] >= 250]
popularity_df = popularity_df.sort_values('avg_ratings', ascending=False).head(50)

# Add author + image
popularity_df = popularity_df.merge(
    books[['Book-Title', 'Book-Author', 'Image-URL-M']],
    on='Book-Title'
).drop_duplicates('Book-Title')


# =========================
# 6. COLLABORATIVE FILTERING
# =========================

# Relaxed thresholds (IMPORTANT FIX)
active_users = ratings_with_name.groupby('User-ID')['Book-Rating'].count() > 50
active_users = active_users[active_users].index

filtered_rating = ratings_with_name[ratings_with_name['User-ID'].isin(active_users)]

popular_books = filtered_rating.groupby('Book-Title')['Book-Rating'].count() >= 20
popular_books = popular_books[popular_books].index

final_ratings = filtered_rating[filtered_rating['Book-Title'].isin(popular_books)]


# =========================
# 7. PIVOT TABLE
# =========================
pt = final_ratings.pivot_table(
    index='Book-Title',
    columns='User-ID',
    values='Book-Rating'
)

pt.fillna(0, inplace=True)


# Normalize titles (for safer matching)
pt.index = pt.index.str.lower()


# =========================
# 8. COSINE SIMILARITY
# =========================
similarity_scores = cosine_similarity(pt)


# =========================
# 9. RECOMMEND FUNCTION
# =========================
def recommend(book_name):
    book_name = book_name.lower()

    if book_name not in pt.index:
        print("❌ Book not found!")
        return

    index = np.where(pt.index == book_name)[0][0]

    similar_items = sorted(
        list(enumerate(similarity_scores[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    print("\n📚 Recommended Books:\n")
    for i in similar_items:
        print(pt.index[i[0]])


import pickle

pickle.dump(popularity_df, open('popular.pkl', 'wb'))
pickle.dump(pt, open('pt.pkl', 'wb'))
pickle.dump(books, open('books.pkl', 'wb'))
pickle.dump(similarity_scores, open('similarity.pkl', 'wb'))