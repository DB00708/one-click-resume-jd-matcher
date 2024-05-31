def generate_job_description(jd_corpus, client):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
          {
            "role": "system",
            "content": """You have to extract a json structure like this:. 
        The structure should include the following fields:
        - company_name
        - company_email
        - company_mobile_no
        - position_title
        - position_summary
        - responsibilities
        - requirements
        - experience_needed
        - skills
        - preferred_qualifications
        - location
    
        Here is an example format (If you are not able to extract any information use "" as value):
    
        {
        "company_name": "Maeris",
        "company_email": "",
        "company_mobile_no": "",
        "position_title": "Data Engineer - AI",
        "position_summary": "Seeking a skilled Data Engineer with expertise in AI data pipelines and AWS infrastructure to join our team.",
        "responsibilities": [
            "Design and implement data pipelines tailored for AI training and model development.",
            "Partner with AI data scientists and engineers to understand data needs and ensure efficient data access."
        ],
        "requirements": [
            "5 to 8 years of experience as a Data Engineer or similar role.",
            "Proven experience with AWS services like S3, Redshift, Glue, Lambda, and Kinesis.",
            "Strong proficiency in Python and SQL."
        ],
        "experience_needed": "5 to 8 years",
        "skills": [
            "Python", "SQL", "AWS (S3, Redshift, Glue, Lambda, Kinesis)", "TensorFlow", "PyTorch",
            "Data warehousing", "Data modeling", "Problem-solving", "Analytical skills",
            "Communication", "Collaboration"
        ],
        "preferred_qualifications": [],
        "location": ""
        }
        """
          },
          {
            "role": "user",
            "content": f'{jd_corpus}'
          }
        ],
        temperature=0.5,
        max_tokens=3000,
        top_p=1
      )

    return response.choices[0].message.content
