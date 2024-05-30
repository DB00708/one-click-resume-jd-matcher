import datetime
from openai import OpenAI
from src.constants import OPEN_AI_KEY
from src.generate_new_resume.generating_docx import create_resume
from src.generate_new_resume.generating_new_resume import generating_resume_based_on_jd, add_skills_to_resume
from src.getting_data.getting_jd_data import extract_sentences
from src.getting_data.getting_user_data import retrieving_user_data
from src.constants import FULL_NAME_KEY, JD_PATH_OR_TEXT, RESUME_PATH
from src.getting_data.user_data_utils import download_nltk_resources_if_needed
from src.llm_integration.conversion_of_jd_corpus_to_json import generate_job_description
from src.llm_integration.generate_new_resume_with_updated_skills import generate_resume_based_on_updated_skills
from src.llm_integration.llm_utils import extract_json_from_response
from src.generate_new_resume.ats_score import calculate_ats_percentage, generating_suggestions_based_on_ats_score


def main(payload):
    download_nltk_resources_if_needed('punkt', 'tokenizers/punkt')
    download_nltk_resources_if_needed('stopwords', 'corpora/stopwords')
    resume_data = retrieving_user_data(payload)
    jd_corpus = extract_sentences(payload)
    print(resume_data)

    client = OpenAI(api_key=OPEN_AI_KEY)
    job_description = generate_job_description(jd_corpus, client)
    job_description = extract_json_from_response(job_description)
    ats_percentage, unmatched_skills, resume_experience, required_years = calculate_ats_percentage(resume_data, job_description)
    suggestion = generating_suggestions_based_on_ats_score(ats_percentage, unmatched_skills, resume_experience, required_years)
    print(f"SUGGESTION: {suggestion}")

    updated_skills = add_skills_to_resume(unmatched_skills)
    updated_resume = generating_resume_based_on_jd(resume_data, updated_skills)

    resume_based_on_updated_skills = generate_resume_based_on_updated_skills(updated_resume, client)
    resume_based_on_updated_skills = extract_json_from_response(resume_based_on_updated_skills)

    create_resume(resume_based_on_updated_skills, SAVED_RESUME_PATH)

    return resume_based_on_updated_skills


if __name__ == '__main__':
    payload = {
        FULL_NAME_KEY: "divyansh bhatia",
        RESUME_PATH: r"src/resources/RESUME.pdf",
        JD_PATH_OR_TEXT: r"src/resources/Generative AI Engineer JD (1).docx"
    }

    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"resume_generated_on_{current_time}.docx"
    SAVED_RESUME_PATH = f"src/resources/{file_name}"

    resume_based_on_updated_skills = main(payload)
