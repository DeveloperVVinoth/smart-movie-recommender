📽️ Smart Movie Recommender
A content-based movie recommendation system built with Python, Pandas, and Scikit-learn. This app suggests movies based on genre, keywords, cast, and director using cosine similarity.

🔥 Ideal for anyone exploring machine learning, recommender systems, or building a personal ML portfolio project.

🚀 Demo
🧠 Try the app on Streamlit ↗

🧠 Features:

📦 Uses TMDB 5000 dataset
🎭 Extracts movie genres, cast, keywords, and director
🧠 Natural language-based recommendation using CountVectorizer
🔍 Recommends movies using cosine similarity
💾 Clean model storage (optimized for GitHub)
🖥️ Deployed with Streamlit (optional)

📁 Folder Structure
graphql
Copy
Edit
smart-movie-recommender/
│
recommender.py          # Core logic for recommendations
build_model.py          # Script to preprocess and save model
app.py                  # Streamlit web app
data/
tmdb_5000_movies.csv
models/
similarity.pkl      # (excluded from GitHub due to size)
gitignore
README.md               


⚙️ Installation & Usage
bash
Copy
Edit
# 1. Clone this repo
git clone https://github.com/DeveloperVVinoth/smart-movie-recommender.git
cd smart-movie-recommender

# 2. Install dependencies
pip install -r requirements.txt

# 3. Build the model
python build_model.py

# 4. Run the app
streamlit run app.py
✅ Make sure to place tmdb_5000_movies.csv inside the data/ folder.

🛠️ Technologies Used
Python

Pandas

Scikit-learn

Streamlit

TMDB Dataset

📌 Future Improvements
Use TF-IDF for better text weighting
Integrate with TheMovieDB API for live data
Add poster previews and trailers
Deploy on HuggingFace Spaces / Streamlit Cloud

Install git lfs if you want the model

👨‍💻 Author
Made with ❤️ by DeveloperVVinoth

📜 License
This project is open source and available under the MIT License.
