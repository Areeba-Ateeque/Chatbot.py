import nltk
import random
import spacy
from nltk.corpus import wordnet as wn

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Preprocessing and Utility Functions
def tokenize(text):
    return nltk.word_tokenize(text)

def lemmatize(text):
    doc = nlp(text)
    return [token.lemma_ for token in doc]

def get_synonyms(word):
    synonyms = set()
    for syn in wn.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)

# Define some patterns and responses
patterns_responses = {
    "hello": ["Hi there!", "Hello!", "Greetings!"],
    "how are you": ["I'm a chatbot, I'm always okay!", "Doing great! How about you?"],
    "bye": ["Goodbye!", "See you later!", "Take care!"]
}

def generate_response(user_input):
    tokens = tokenize(user_input.lower())
    lemmas = lemmatize(user_input.lower())
    
    for pattern in patterns_responses:
        if pattern in lemmas or any(lemma in get_synonyms(pattern) for lemma in lemmas):
            return random.choice(patterns_responses[pattern])
    return "I'm not sure I understand. Can you please rephrase?"

# Start a simple chat loop
def chat():
    print("Chatbot: Hi! How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        response = generate_response(user_input)
        print(f"Chatbot: {response}")

# Start the chat
if __name__ == "__main__":
    chat()
    