import subprocess

def ask_fitbot(query):
    prompt = f"You are a stylist bot. Answer this question: {query}"
    result = subprocess.run(["ollama", "run", "tinyllama", prompt], capture_output=True, text=True)
    return result.stdout.strip()
