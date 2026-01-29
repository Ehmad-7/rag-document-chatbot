
def build_memory_context(history,max_turns=1):
    recent=history[-max_turns:]
    text=''
    for q,a in recent:
        text+=f"User: {q}\nAssistant: {a}\n"
    return text