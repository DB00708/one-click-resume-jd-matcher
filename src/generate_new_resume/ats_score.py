from src.constants import EXPERIENCE_THRESHOLD


def calculate_ats_percentage(resume, job_description):
    resume_skills = set(resume.get('skills', []))
    resume_experience = resume.get('experience', 0)
    job_skills = set(job_description.get('skills', []))
    experience_needed = job_description.get('experience_needed', 0)

    matching_skills_count = len(resume_skills.intersection(job_skills))
    unmatched_skills = job_skills - resume_skills

    experience_score = 0

    if 'years' in experience_needed:
        required_years = int(''.join(filter(str.isdigit, experience_needed)))
        if required_years > 0:
            experience_score = min(required_years, resume_experience)
    else:
        required_years = 0
        experience_score = 0

    total_possible_score = (len(job_skills) * 1) + required_years
    total_score = matching_skills_count + experience_score

    ats_percentage = (total_score / total_possible_score) * 100

    return ats_percentage, unmatched_skills, resume_experience, required_years


def generating_suggestions_based_on_ats_score(ats_percentage, unmatched_skills, resume_experience, required_years):
    experience_percentage = resume_experience/required_years * 100 if required_years != 0 else 100
    if experience_percentage > EXPERIENCE_THRESHOLD:
        if ats_percentage < 50:
            return f"Your ATS score is below 50%, which means there are significant gaps between your skills and the job requirements. Consider updating your experience or adding relevant skills. You can consider updating your resume with the following skills: {unmatched_skills}"
        elif 50 <= ats_percentage < 75:
            return "Your ATS score is between 50% and 75%, indicating some alignment with the job requirements. Consider updating your experience or adding more skills to improve your score."
        elif ats_percentage >= 75:
            return "Congratulations! Your ATS score is above 75%, indicating a strong alignment with the job requirements."
    return f"You are not experienced enough to get the role as required experience is {required_years} years and your current experience is {resume_experience} years"
