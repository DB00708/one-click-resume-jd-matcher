def generate_resume_based_on_updated_skills(updated_skills_resume, client):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": """You are an expert in creating professional resumes. You will be provided with a JSON structure containing a resume. Your task is to improve the resume based on the updated skills provided. Ensure that the resume remains professional, well-structured, and follows the standard resume format. Return the updated resume in the same JSON structure with enhancements made where necessary.

The JSON structure of the resume is as follows:
{
    "full_name": "string",
    "user_email": "string",
    "user_mobile_no": "string",
    "skills": ["string", ...],
    "education": [
        {
            "degree": "string",
            "university": "string",
            "duration": "string",
            "board": "string",  # optional
            "school": "string",  # optional
            "percentage": "string",  # optional
            "year": "string"  # optional
        },
        ...
    ],
    "projects": [
        {
            "title": "string",
            "duration": "string",
            "description": "string"
        },
        ...
    ],
    "responsibility": [
        {
            "role": "string",
            "organization": "string",
            "duration": "string",
            "responsibilities": ["string", ...]
        }
    ],
    "achievements": [
        {
            "title": "string",
            "organization": "string",
            "details": "string"
        },
        ...
    ],
    "training": [
        {
            "title": "string",
            "duration": "string",
            "details": "string"
        },
        ...
    ]
}
"""
            },
            {
                "role": "user",
                "content": f'{updated_skills_resume}'
            }
        ],
        temperature=0.5,
        max_tokens=3000,
        top_p=1
    )

    return response.choices[0].message.content
