# MovieChatbot
School project implementing a Flask-based movie recommendation system using Python, applying scikit-learn for data preprocessing, clustering algorithms, and similarity-based recommendations

**Status:** In progress
## Technologies Used 
- Python 3 
- Flask 
- scikit-learn 
- NumPy / Pandas
- HTML/CSS 
- Kaggle movie dataset
 
## Features: 
- Flask-based web interface for entering movie queries. 
- Machine learning recommendation engine using clustering + similarity metrics. 
- Data preprocessing and feature extraction using scikit-learn. 
- Uses a Kaggle movie dataset that is cleaned and prepared within the project. 
- Returns a list of similar movies based on computed recommendation scores. 

## Project Structure 
project/
│── application.py # Main Flask application.
│── recommender/
│ ├── __init__.py # Makes recommender a Python package.
│ └── recommend.py # Recommendation + similarity logic.
│── data/
│ └── movies.csv # Raw dataset.
│── templates/
│ └── index.html # Web interface template.
│── static/
│ └── styles.css # Optional CSS for styling.
│── requirements.txt # Python dependencies.
└── README.md

## How It Works 

### **1. Data Loading & Preprocessing.**
- Loads a movie dataset sourced from Kaggle. 
- Cleans missing values and extracts relevant features. 
- Converts categorical fields into numerical representations as needed. 
- Produces feature vectors used for clustering and similarity scoring. 

### **2. Clustering.**
- A clustering algorithm (e.g., KMeans) groups movies with similar characteristics 
- Reduces search space to find related movies efficiently. 

### **3. Similarity Computation.**
- Locates the user-provided movie in the dataset. 
- Computes similarity metrics (e.g., cosine similarity). 
- Ranks the closest matching movies to generate recommendations. 

### **4. Flask Web Application.**
- User enters a movie title 
- Back end retrieves movie data, computes similarity, and returns recommendations 
- UI displays the top similar movies through an HTML template 

## Running the Project Locally:
### 1. Clone the repository:
```bash
git clone https://github.com/hln-v/MovieChatbot.git
cd MovieChatbot
```

### 2. Install dependencies:
 pip install -r requirements.txt
 
### 3. Run the Flask app:
 python application.py

### 4. Open browser:
 http://127.0.0.1:5000/

# This project was created for a university computer science course. It demonstrates:

- Python and Flask development.

- Machine learning workflows.

- Data preprocessing.

- Clustering algorithms.

- Recommendation system design.

- Software project structure and packaging.

# Future Improvements

- Support genre-based or rating-based queries.

- Add user session support.

- Improve UI and layout.

- Experiment with additional similarity metrics.