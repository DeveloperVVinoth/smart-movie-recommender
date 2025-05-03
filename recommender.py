import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Step 1: Load the movie dataset
def load_data(movies_path="data/tmdb_5000_movies.csv", credits_path="data/tmdb_5000_credits.csv"):
    movies = pd.read_csv(movies_path)
    credits = pd.read_csv(credits_path)

    # Merge on title
    movies = movies.merge(credits, on="title")
    return movies


# Step 2: Preprocess and combine important columns
def preprocess(movies):
    # We'll use these 4 columns
    movies = movies[['title', 'genres', 'keywords', 'cast', 'crew']].copy()
    movies.dropna(inplace=True)

    # Convert JSON-like strings into text
    def extract_names(obj):
        try:
            return " ".join([d['name'] for d in eval(obj)])
        except:
            return ""

    def extract_director(obj):
        try:
            for d in eval(obj):
                if d['job'] == 'Director':
                    return d['name'].replace(" ", "")
        except:
            return ""
        return ""

    movies['genres'] = movies['genres'].apply(extract_names)
    movies['keywords'] = movies['keywords'].apply(extract_names)
    movies['cast'] = movies['cast'].apply(lambda x: " ".join([d['name'] for d in eval(x)[:3]]))
    movies['director'] = movies['crew'].apply(extract_director)

    # Combine into a single text column
    movies['tags'] = movies['genres'] + " " + movies['keywords'] + " " + movies['cast'] + " " + movies['director']
    return movies[['title', 'tags']]

# Step 3: Create and save similarity model
def build_model(movies):
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(movies['tags']).toarray()
    similarity = cosine_similarity(vectors)

    # Save for later use
    with open("models/similarity.pkl", "wb") as f:
        pickle.dump((movies, similarity), f)

    print("✅ Model saved to models/similarity.pkl")
