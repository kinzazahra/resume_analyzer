from flask import Flask, render_template, request
import os
from utils.parser import extract_text
from utils.skills import extract_skills
from utils.matcher import get_similarity

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/', methods=['GET', 'POST'])
def home():
    result = {}

    if request.method == 'POST':
        file = request.files['resume']
        job_desc = request.form['job_desc']

        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        text = extract_text(filepath)

        resume_skills = extract_skills(text)
        job_skills = extract_skills(job_desc.lower())

        # fallback if no skills found
        if not job_skills:
            job_skills = job_desc.lower().split()

        score = get_similarity(text, job_desc.lower())

        missing_skills = list(set(job_skills) - set(resume_skills))

        result = {
            "score": score,
            "resume_skills": resume_skills,
            "job_skills": job_skills,
            "missing": missing_skills
        }

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)