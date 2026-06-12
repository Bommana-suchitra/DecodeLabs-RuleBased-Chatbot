from datetime import datetime
import random

GREETINGS = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi there!",
    "hey": "Hey! Nice to see you.",
    "good morning": "Good morning! Have a productive day.",
    "good evening": "Good evening! Hope you're doing well."
}

FAREWELLS = {
    "bye": "Goodbye! Have a great day.",
    "exit": "Exiting chatbot...",
    "quit": "See you next time!"
}

IDENTITY = {
    "who are you": "I am IntelliBot, a rule-based AI chatbot.",
    "what can you do": "I can chat, tell jokes, provide quotes, calculate expressions, track history, and more."
}

QUOTES = [
    "Success is the sum of small efforts repeated daily.",
    "Believe in yourself and all that you are.",
    "Consistency beats motivation.",
    "Learning never exhausts the mind."
]

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the computer cold? It left its Windows open.",
    "Why do Java developers wear glasses? Because they don't C#."
]

MOODS = {
    "sad": "I'm sorry you're feeling sad. Better days are ahead.",
    "happy": "That's wonderful! Keep smiling.",
    "angry": "Take a deep breath. Stay calm and focused.",
    "stressed": "Try taking a short break and relaxing."
}


def get_time():
    return datetime.now().strftime("%H:%M:%S")


def get_date():
    return datetime.now().strftime("%d-%m-%Y")


def get_day():
    return datetime.now().strftime("%A")


def get_quote():
    return random.choice(QUOTES)


def get_joke():
    return random.choice(JOKES)