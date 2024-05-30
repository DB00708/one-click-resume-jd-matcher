def add_skills_to_resume(unmatched_skills):
    updated_skills = []

    for skill in unmatched_skills:
        while True:
            choice = input(f"Do you want to add '{skill}' to your new resume? (y/n): ").lower()
            if choice == 'y':
                experience = input(f"Do you have experience with '{skill}'? (y/n): ").lower()
                if experience == 'y':
                    updated_skills.append(skill)
                    break
                if experience == 'n':
                    continue
                else:
                    print("Please enter a valid choice (y/n).")
            elif choice == 'n':
                break
            else:
                print("Please enter a valid choice (y/n).")

    return updated_skills


def generating_resume_based_on_jd(resume_data, updated_skills):
    old_skills = resume_data["skills"]
    new_skills = old_skills + updated_skills
    resume_data["skills"] = new_skills
    return resume_data
