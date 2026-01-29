import re

def parse_resume(text):
    fields = {}

    patterns = {
        "education": r"(Education|EDUCATION)(.*?)(Skills|SKILLS|Experience|$)",
        "skills": r"(Skills|SKILLS)(.*?)(Experience|EDUCATION|$)",
        "experience": r"(Experience|EXPERIENCE)(.*?)(Projects|$)",
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.DOTALL)
        if match:
            fields[key] = match.group(2).strip().replace("\n", " ")

    return fields


def answer_resume(question, resume_fields):
    q = question.lower()

    if "education" in q:
        return resume_fields.get("education", "Education not found in resume.")

    if "skill" in q:
        return resume_fields.get("skills", "Skills not found in resume.")

    if "experience" in q:
        return resume_fields.get("experience", "Experience not found in resume.")

    return "I can answer questions about education, skills, and experience."
