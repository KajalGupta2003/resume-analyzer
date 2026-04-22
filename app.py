import streamlit as st
from utils.parser import extract_text
from utils.skills import extract_skills, extract_job_skills, skill_gap
from utils.scorer import final_score, ml_match_score
from utils.suggestions import get_suggestions

st.title("📄 Smart Resume Analyzer")
st.markdown("### AI-powered Resume Analysis using NLP 🚀")
st.write("---")

file = st.file_uploader("Upload Resume", type=["pdf"])
job_desc = st.text_area("Paste Job Description")

if st.button("Analyze"):
    if file and job_desc:
        text = extract_text(file)

        # ✅ Extract skills
        resume_skills = extract_skills(text)
        job_skills = extract_job_skills(job_desc)

        # 🔥 SHOW extracted skills (for debugging / clarity)
        st.write("Resume Skills:", resume_skills)
        st.write("Job Skills:", job_skills)

        # ✅ CHECK if job skills empty (ADD HERE 👇)
        if not job_skills:
            st.warning("⚠️ No skills detected from job description. Try adding proper keywords like Python, React, SQL.")
        
        # ✅ Skill gap
        missing = skill_gap(resume_skills, job_skills)

        # ✅ ML scoring
        job_score = ml_match_score(text, job_desc)
        score = final_score(resume_skills, job_score, text)

        # ✅ Suggestions
        suggestions = get_suggestions(text, resume_skills, score)

        # 🎯 RESULTS UI
        st.subheader("📊 Results")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("📄 Resume Score", f"{score}/100")
        with col2:
            st.metric("🎯 Job Match", f"{job_score}%")

        st.progress(int(score))
        st.write("---")

        # ✅ Skills
        st.subheader("✅ Skills Found")
        st.write(resume_skills)

        # ✅ Job Skills
        st.subheader("🧠 Job Required Skills")
        st.write(job_skills)

        # ✅ Missing Skills
        st.subheader("📉 Missing Skills (Based on Job)")
        st.write(missing)

        # ✅ Suggestions
        st.subheader("💡 Suggestions")
        for s in suggestions:
            st.warning(s)

    else:
        st.error("Upload file and enter job description")