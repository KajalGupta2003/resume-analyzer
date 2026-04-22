from data.skills_list import SKILLS

def extract_skills(text):
    text = text.lower()
    found = [skill for skill in SKILLS if skill in text]
    return found