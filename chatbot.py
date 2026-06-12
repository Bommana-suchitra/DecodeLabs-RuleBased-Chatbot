from intents import *
from utils import *

class SessionManager:
    def __init__(self):
        self.user_name = None
        self.history = []
        self.total_messages = 0
        self.known_queries = 0
        self.unknown_queries = 0


class ChatBot:

    def __init__(self):
        self.session = SessionManager()

    def process_input(self, user_input):

        self.session.total_messages += 1
        self.session.history.append(user_input)

        # Greetings
        if user_input in GREETINGS:
            self.session.known_queries += 1
            return GREETINGS[user_input]

        # Farewells
        if user_input in FAREWELLS:
            self.session.known_queries += 1
            return FAREWELLS[user_input]

        # Identity
        if user_input in IDENTITY:
            self.session.known_queries += 1
            return IDENTITY[user_input]

        # Date Time Day
        if user_input == "time":
            self.session.known_queries += 1
            return get_time()

        if user_input == "date":
            self.session.known_queries += 1
            return get_date()

        if user_input == "day":
            self.session.known_queries += 1
            return get_day()

        # Quotes
        if user_input in ["quote", "motivate me"]:
            self.session.known_queries += 1
            return get_quote()

        # Jokes
        if user_input in ["joke", "tell joke"]:
            self.session.known_queries += 1
            return get_joke()

        # Name Memory
        if "my name is" in user_input:
            name = extract_name(user_input)

            if name:
                self.session.user_name = name.title()
                self.session.known_queries += 1
                return f"Nice to meet you, {self.session.user_name}!"

        if user_input == "what is my name":
            self.session.known_queries += 1

            if self.session.user_name:
                return f"Your name is {self.session.user_name}"
            return "I don't know your name yet."

        # Mood Detection
        for mood in MOODS:
            if mood in user_input:
                self.session.known_queries += 1
                return MOODS[mood]

        # Calculator
        if user_input.startswith("calculate"):
            self.session.known_queries += 1
            expression = user_input.replace("calculate", "").strip()
            return calculate_expression(expression)

        # History
        if user_input == "history":
            self.session.known_queries += 1

            if not self.session.history:
                return "No history found."

            return "\n".join(self.session.history)

        if user_input == "clear history":
            self.session.known_queries += 1
            self.session.history.clear()
            return "History cleared."

        # Statistics
        if user_input == "stats":
            self.session.known_queries += 1

            return (
                f"Total Messages: {self.session.total_messages}\n"
                f"Known Queries: {self.session.known_queries}\n"
                f"Unknown Queries: {self.session.unknown_queries}"
            )

        # Help
        if user_input == "help":
            self.session.known_queries += 1

            return """
Available Commands:

hello
bye
time
date
day
quote
motivate me
tell joke
my name is <name>
what is my name
calculate 10+20
history
clear history
stats
help
"""

        self.session.unknown_queries += 1
        return "Sorry, I don't understand that command."

    def run(self):

        print("=" * 50)
        print("        INTELLIBOT AI CHATBOT")
        print("=" * 50)
        print("Type 'help' to see commands.")
        print("Type 'exit' to quit.\n")

        while True:

            raw_input_text = input("You: ")
            user_input = sanitize_input(raw_input_text)

            response = self.process_input(user_input)

            print("Bot:", response)

            if user_input in ["exit", "quit", "bye"]:
                break


if __name__ == "__main__":
    bot = ChatBot()
    bot.run()