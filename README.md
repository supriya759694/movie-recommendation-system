# 🎬 Movie Recommender System

A content-based Movie Recommendation System built using **Python**, **Pandas**, **Scikit-Learn**, and **Streamlit**. The application recommends similar movies 
based on movie metadata such as genres, cast, crew, keywords, and overview, and displays movie posters using the TMDB API.

## 🚀 Live Demo

**Live Application:**
https://movie-recommendation-system-syvww9ywfxeajcrigd5ynq.streamlit.app/

## 📂 GitHub Repository

**Source Code:**
https://github.com/supriya759694/movie-recommendation-system

---

## 📖 Project Overview

This project uses a **content-based filtering approach** to recommend movies similar to the movie selected by the user.

The recommendation engine analyzes movie features such as:

* Genres
* Keywords
* Cast
* Crew
* Movie Overview

The textual information is combined into a single feature and transformed into vectors using **CountVectorizer**. Similarity between movies is calculated using **Cosine Similarity**.

---

## ✨ Features

* Interactive Streamlit Web Application
* Content-Based Movie Recommendation Engine
* TMDB API Integration for Movie Posters
* Fast Similarity Search
* User-Friendly Interface
* Cloud Deployment with Streamlit Community Cloud

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Libraries & Frameworks

* Streamlit
* Pandas
* NumPy
* Scikit-Learn
* Requests
* Pickle

### Machine Learning & NLP

* CountVectorizer
* Cosine Similarity
* Content-Based Filtering

### Deployment

* Streamlit Community Cloud

### Dataset

* TMDB 5000 Movies Dataset
* TMDB 5000 Credits Dataset
* dataset link : https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
---

## ⚙️ How It Works

1. Load movie metadata.
2. Combine relevant movie features into a single text representation.
3. Convert text into vectors using CountVectorizer.
4. Calculate cosine similarity between movies.
5. Find the most similar movies.
6. Fetch movie posters using the TMDB API.
7. Display recommendations through a Streamlit web interface.

---

## 📸 Application Workflow

```text
User Selects a Movie
          ↓
Feature Extraction
          ↓
CountVectorizer
          ↓
Cosine Similarity
          ↓
Top Similar Movies
          ↓
TMDB Poster Fetching
          ↓
Display Recommendations
```

## 📁 Project Structure

```text
movie-recommendation-system/
│
├── app.py
├── movies.pkl
├── requirements.txt
├── .gitignore
├── Movie_recommendation.ipynb
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
└── README.md
```

## 💻 Local Setup

### Clone Repository

```bash
git clone https://github.com/supriya759694/movie-recommendation-system.git
```

### Move to Project Directory

```bash
cd movie-recommendation-system
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 🎯 Future Improvements

* Collaborative Filtering Recommendations
* User Authentication
* Movie Search Functionality
* Trending Movies Section
* Personalized Recommendations
* Enhanced UI/UX Design
* Hybrid Recommendation System

---

## 👩‍💻 Author

**Supriya Bhowmick**

B.Tech (Information Technology) | Software Engineer | Full-Stack Developer | Machine Learning Enthusiast

### Connect With Me

* GitHub: https://github.com/supriya759694
* LinkedIn: https://www.linkedin.com/in/supriya-bhowmick-b31181227/

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub. It helps showcase the project and supports future development.

---

## 📄 License

This project is intended for educational and portfolio purposes.
