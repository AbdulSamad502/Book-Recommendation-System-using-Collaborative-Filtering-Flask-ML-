from flask import Flask, render_template, request
import pickle
import numpy as np
import os
import gdown

app = Flask(__name__)

# =========================
# 1. DOWNLOAD FILES (IF NOT PRESENT)
# =========================

files = {
    "pt.pkl": "https://drive.google.com/uc?id=1KcVZdhOdGGSJufmgHWX2s-ncrIiYY8gR",
    "similarity.pkl": "https://drive.google.com/uc?id=1n-5zUwWQnOrAvywnHcwYJVx0-pFsSlfs",
    "books.pkl": "https://drive.google.com/uc?id=13nnsGfbRrPXlOOgvna5mC6cx7fjakBJm",
    "popular.pkl": "https://drive.google.com/uc?id=1xOeJ4Z3w6FLBXKDwuX2GWBZG8Vu8KZ4T"
}

for file, url in files.items():
    if not os.path.exists(file):
        print(f"⬇️ Downloading {file}...")
        gdown.download(url, file, quiet=False)

print("✅ All model files ready!")


# =========================
# 2. LOAD DATA
# =========================

popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity.pkl', 'rb'))

# Normalize titles for matching
pt.index = pt.index.str.lower()


# =========================
# 3. HOME PAGE
# =========================

@app.route('/')
def index():
    return render_template(
        'index.html',
        book_name=list(popular_df['Book-Title'].values),
        author=list(popular_df['Book-Author'].values),
        image=list(popular_df['Image-URL-M'].values),
        votes=list(popular_df['num_ratings'].values),
        rating=list(popular_df['avg_ratings'].values)
    )


# =========================
# 4. RECOMMEND PAGE
# =========================

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')


# =========================
# 5. RECOMMENDATION LOGIC
# =========================

@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')

    if not user_input:
        return render_template('recommend.html', error="Please enter a book name!")

    user_input = user_input.lower()

    if user_input not in pt.index:
        return render_template('recommend.html', error="❌ Book not found!")

    index = np.where(pt.index == user_input)[0][0]

    similar_items = sorted(
        list(enumerate(similarity_scores[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    data = []

    for i in similar_items:
        book_title = pt.index[i[0]]

        temp_df = books[books['Book-Title'].str.lower() == book_title]

        # Safety check
        if temp_df.empty:
            continue

        item = [
            book_title.title(),
            temp_df['Book-Author'].values[0],
            temp_df['Image-URL-M'].values[0]
        ]

        data.append(item)

    return render_template('recommend.html', data=data)


# =========================
# 6. RUN APP
# =========================

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # dynamic port
    app.run(host="0.0.0.0", port=port)