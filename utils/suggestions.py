from data.skills_list import SKILLS

def get_missing_skills(found_skills):
    missing = [s for s in SKILLS if s not in found_skills]
    return missing[:5]


def get_suggestions(text, skills, score):
    suggestions = []

    text = text.lower()

    if "experience" not in text:
        suggestions.append("Add an Experience section")

    if "project" not in text:
        suggestions.append("Add Projects section")

    if len(text.split()) < 300:
        suggestions.append("Increase resume content")
    if len(skills) < 5:
        suggestions.append("Add more technical skills")

    if score < 60:
        suggestions.append("Your resume needs improvement")

    return suggestions