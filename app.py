import streamlit as st
from utils.parser import extract_text
from utils.skills import extract_skills
from utils.scorer import match_score, final_score
from utils.suggestions import get_missing_skills, get_suggestions

st.title("📄 Resume Analyzer")

file = st.file_uploader("Upload Resume", type=["pdf"])
job_desc = st.text_area("Paste Job Description")

if st.button("Analyze"):
    if file and job_desc:
        text = extract_text(file)

        skills = extract_skills(text)
        job_score = match_score(text, job_desc)
        score = final_score(skills, job_score)

        missing = get_missing_skills(skills)
        suggestions = get_suggestions(text, skills, score)

        st.subheader("📊 Results")
        st.write(f"Score: {score}/100")
        st.progress(int(score))

        st.subheader("✅ Skills Found")
        st.write(skills)

        st.subheader("❌ Missing Skills")
        st.write(missing)

        st.subheader("💡 Suggestions")
        for s in suggestions:
            st.warning(s)
    else:
        st.error("Upload file and enter job description")