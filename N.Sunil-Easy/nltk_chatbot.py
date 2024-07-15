# Basic Chatbot with NLTK
# Required Modules
import nltk
from nltk.chat.util import Chat, reflections

# Pairs
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"how are you?",
        ["I'm good, thank you! How about you?", "Doing well, how are you?"]
    ],
    [
        r"what is your name?",
        ["I'm a chatbot created using NLTK.", "You can call me NLTKBot."]
    ],
    [
        r"what can you do?",
        ["I can chat with you and answer some basic questions.", "I'm here to talk and help you with basic queries."]
    ],
    [
        r"how does natural language processing work?",
        ["Natural Language Processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers and humans through natural language.", 
         "NLP combines computational linguistics with statistical, machine learning, and deep learning models to process and understand human language."]
    ],
    [
        r"(.*) your favorite (.*)?",
        ["I'm just a bot, but I think everything is interesting!", "I don't have preferences, but I enjoy learning new things!"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon!", "Goodbye! It was nice talking to you."]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that. Can you please rephrase?", "Can you please clarify your question?"]
    ]
]

# Converse ChatBot
def chatbot():
    print("Hi! I'm a chatbot created using NLTK. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Start ChatBot
if __name__ == "__main__":
    chatbot()
