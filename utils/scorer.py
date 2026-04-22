def match_score(resume_text, job_desc):
    r = set(resume_text.lower().split())
    j = set(job_desc.lower().split())

    if len(j) == 0:
        return 0

    match = r.intersection(j)
    return round(len(match) / len(j) * 100, 2)


def final_score(skills, job_score):
    score = 0

    score += len(skills) * 5     # skills weight
    score += job_score * 0.5     # job match weight
    score += 20                  # base score

    return min(score, 100)