import spacy
from data.skills_list import SKILLS

# load model once
nlp = spacy.load("en_core_web_sm")


# ✅ Extract skills from text using spaCy
def extract_skills(text):
    doc = nlp(text.lower())

    tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]

    found_skills = []
    for skill in SKILLS:
        skill_words = skill.split()

        # check if all words of skill exist in tokens
        if all(word in tokens for word in skill_words):
            found_skills.append(skill)

    return list(set(found_skills))


# ✅ Extract job skills
def extract_job_skills(job_desc):
    return extract_skills(job_desc)


# ✅ Skill gap
def skill_gap(resume_skills, job_skills):
    resume_set = set(resume_skills)
    job_set = set(job_skills)

    return list(job_set - resume_set)