# 📚 Book Recommendation System

A machine learning-based book recommendation system that suggests books based on user preferences using **Collaborative Filtering**.

---

## 🚀 Features

- 🔥 Top 50 Popular Books
- 🔍 Search any book and get recommendations
- 📊 Based on cosine similarity
- ⚡ Fast performance using precomputed pickle files
- 🎨 Clean UI with Flask + HTML + CSS

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- HTML/CSS

---

## 📁 Project Structure
BRS/
│
├── app.py
├── main.py
├── requirements.txt
├── .gitignore
│
├── templates/
│ ├── index.html
│ └── recommend.html
│
├── static/
│ └── style.css
│
├── popular.pkl
├── pt.pkl
├── books.pkl
├── similarity.pkl


---

## ⚙️ Installation

### 1. Clone repo
```bash
git clone https://github.com/your-username/book-recommendation-system.git
cd book-recommendation-system


---

## ⚙️ Installation

### 1. Clone repo
```bash
git clone https://github.com/your-username/book-recommendation-system.git
cd book-recommendation-system
2. Create virtual environment
python -m venv venv
3. Activate environment
venv\Scripts\activate
4. Install dependencies
pip install -r requirements.txt
▶️ Run the app
python app.py

Open in browser:

http://127.0.0.1:5000/
🧠 How it Works

Filters active users and popular books

Creates a user-book matrix

Applies cosine similarity

Recommends top 5 similar books


---

## ⚙️ Installation

### 1. Clone repo
```bash
git clone https://github.com/your-username/book-recommendation-system.git
cd book-recommendation-system
2. Create virtual environment
python -m venv venv
3. Activate environment
venv\Scripts\activate
4. Install dependencies
pip install -r requirements.txt
▶️ Run the app
python app.py

Open in browser:

http://127.0.0.1:5000/
🧠 How it Works

Filters active users and popular books

Creates a user-book matrix

Applies cosine similarity

Recommends top 5 similar books

👨‍💻 Author

Abdul Samad


---

# 🎯 Final Checklist

✅ Virtual env created  
✅ Dependencies installed  
✅ requirements.txt ready  
✅ .gitignore ready  
✅ README ready  
✅ GitHub title + description ready  

---

# 🚀 Next Step (VERY IMPORTANT)

Now do:
```bash
git init
git add .
git commit -m "Initial commit - Book Recommendation System"
git branch -M main
git remote add origin <your-repo-link>
git push -u origin main