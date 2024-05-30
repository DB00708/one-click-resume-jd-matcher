def generating_resume_based_on_jd(resume_data, unmatched_skills):
    old_skills = resume_data["skills"]
    new_skills = old_skills + list(unmatched_skills)
    resume_data["skills"] = new_skills
    return resume_data
