def load_skills():
    with open('skills_db.txt', 'r') as f:
        skills = f.read().splitlines()
    return skills

def extract_skills(text):
    skills_db = load_skills()
    found = []

    for skill in skills_db:
        if skill in text:
            found.append(skill)

    return list(set(found))