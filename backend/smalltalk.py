def handle_small_talk(question):
    q = question.lower().strip()
    greetings = ["hi", "hello", "hey", "good morning", "good afternoon", "good evening", "how are you?"]

    if q in greetings:
        return "Hi! Ask me about the documents or the resume."
    return None