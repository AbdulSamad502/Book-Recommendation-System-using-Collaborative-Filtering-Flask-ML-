# 📚 Book Recommendation System

A machine learning-based book recommendation system that suggests books based on user preferences using **Collaborative Filtering**.

---

## 🚀 Features

- 🔥 Top 50 Popular Books
- 🔍 Search any book and get recommendations
- 📊 Based on cosine similarity
- ⚡ Fast performance using precomputed model files
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


> ⚠️ Note: `.pkl` files and datasets are not included in this repository due to size limitations.

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/book-recommendation-system.git
cd book-recommendation-system
2. Create virtual environment
python -m venv venv
3. Activate environment
Windows:
venv\Scripts\activate
Mac/Linux:
source venv/bin/activate
4. Install dependencies
pip install -r requirements.txt
▶️ Run the App
python app.py

Open in browser:

http://127.0.0.1:5000/
🚀 Deployment

This project handles large model files using Google Drive integration.

.pkl files are NOT stored in GitHub

They are automatically downloaded during runtime

🔧 Deployment Steps (Render)

Push your code to GitHub

Go to https://render.com

Create a new Web Service

Connect your GitHub repo

Settings:

Build Command

pip install -r requirements.txt

Start Command

python app.py
⚡ First Run Behavior

Downloads model files from Google Drive

Takes some time ⏳

⚡ Next Runs

Loads instantly ⚡

🧠 How It Works

Filters active users and popular books

Creates a user-item matrix (pivot table)

Computes similarity using cosine similarity

Recommends top 5 similar books

🔥 Future Improvements

Hybrid recommendation system (Content + Collaborative)

Autocomplete search

Better UI (Netflix-style)

Cloud deployment optimization

👨‍💻 Author

Abdul Samad

⭐ If you like this project

Give it a ⭐ on GitHub!

