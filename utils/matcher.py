from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_similarity(resume_text, job_desc):
    cv = CountVectorizer()

    matrix = cv.fit_transform([resume_text, job_desc])
    score = cosine_similarity(matrix)[0][1]

    return round(score * 100, 2)