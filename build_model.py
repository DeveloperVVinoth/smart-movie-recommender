from recommender import load_data, preprocess, build_model

# Load data
movies = load_data()

# Preprocess data
cleaned = preprocess(movies)

# Build and save similarity model
build_model(cleaned)
