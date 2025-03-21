# bot.py
import sys
import json

# Simple Q&A dataset (You can later load this from a separate JSON file)
qa_pairs = {
    "what is your notice period": "My notice period is 30 days.",
    "what is your current ctc": "My current CTC is confidential. Please contact me directly.",
    "what is your preferred location": "I'm open to remote or Bangalore-based opportunities.",
    "are you open to relocation": "Yes, I’m open to relocation depending on the opportunity.",
}

def answer_question(question):
    q = question.lower().strip()
    for key in qa_pairs:
        if key in q:
            return qa_pairs[key]
    return "Thank you for your question. I'll get back to you soon!"

if __name__ == "__main__":
    question = sys.argv[1]
    print(answer_question(question))
