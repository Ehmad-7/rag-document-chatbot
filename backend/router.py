def route(question):
    q = question.lower()

    resume_keywords = ["cv", "resume", "skill", "education", "experience", "profile"]

    for k in resume_keywords:
        if k in q:
            return "resume"

    return "knowledge"
