def load_skills():
    import os

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(BASE_DIR, 'skills_db.txt')

    with open(file_path, 'r') as f:
        skills = f.read().splitlines()

    return skills


def extract_skills(text):
    skills_db = load_skills()
    found = []

    for skill in skills_db:
        if skill in text:
            found.append(skill)

    return list(set(found))