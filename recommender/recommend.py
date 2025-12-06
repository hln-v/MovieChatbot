import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Load dataset
df = pd.read_csv("data/movies_metadata.csv", low_memory=False)

# 2. Keep only needed columns and rows that have an overview
df = df[["title", "overview", "release_date"]].dropna(subset=["overview", "title"])

# Reset index just to be safe
df = df.reset_index(drop=True)

# 3. Create a TF-IDF matrix over the overview text
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["overview"])

def get_recommendations(user_message: str, top_k: int = 3):
    """
    Use TF-IDF cosine similarity to find movies whose overview
    is similar to the user's description.
    """

    # If user input is empty, just return some popular/random movies
    if not user_message.strip():
        sample = df.sample(min(top_k, len(df)))
        results = []
        for _, row in sample.iterrows():
            release_date = str(row.get("release_date", ""))
            year = release_date[:4] if isinstance(release_date, str) and len(release_date) >= 4 else ""
            results.append({
                "title": row["title"],
                "year": year,
                "synopsis": row["overview"],
            })
        return results

    # 4. Transform the user query into TF-IDF vector
    query_vec = tfidf.transform([user_message])

    # 5. Compute cosine similarity between query and all movie overviews
    cosine_similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()

    # 6. Get indices of top_k most similar movies
    top_indices = cosine_similarities.argsort()[::-1][:top_k]

    results = []
    for idx in top_indices:
        row = df.iloc[idx]
        release_date = str(row.get("release_date", ""))
        year = release_date[:4] if isinstance(release_date, str) and len(release_date) >= 4 else ""

        results.append({
            "title": row["title"],
            "year": year,
            "synopsis": row["overview"],
        })

    return results

