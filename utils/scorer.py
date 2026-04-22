from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ✅ ML-based matching (TF-IDF)
def ml_match_score(resume_text, job_desc):
    if not job_desc.strip():
        return 0

    documents = [resume_text, job_desc]

    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    return round(similarity[0][0] * 100, 2)


# ✅ Section-based scoring
def section_score(text):
    text = text.lower()
    score = 0

    if "education" in text:
        score += 10
    if "project" in text:
        score += 10
    if "experience" in text:
        score += 10

    return score


# ✅ Final combined score
def final_score(skills, job_score, text):
    score = 0

    # Skills (max ~30)
    score += min(len(skills) * 5, 30)

    # Job match (max 40)
    score += job_score * 0.4

    # Sections (max 30)
    score += section_score(text)

    return round(min(score, 100), 2)