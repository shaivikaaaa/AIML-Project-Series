class SimpleChatbot:
    def __init__(self) -> None:
        self.previous_interactions = []
        self.greet = ["hello", "hi", "good morning", "hey", "good afternoon"]
        self.basic_questions = {
            "how are you?": "I am a machine! So I am always good.",
            "i am really sad today": "Oh! I am sorry to hear this, what can I do to make you feel better?",
            "what's your name?": "I am SimpleBot, your friendly chatbot.",
            "what can you do?": "I can chat with you and remember our conversations!",
            "what's the weather like?": "I don't have real-time weather information, but you can check online.",
            "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!"
        }
        self.farewell = ["bye", "goodbye", "see you later"]
        self.questions_asked = 0

    def answer_question(self, question):
        question = question.lower().strip()
        if question in self.greet:
            response = "Hello! How can I assist you today?"
        elif question in self.basic_questions:
            response = self.basic_questions[question]
        else:
            response = "Sorry, I don't understand this."
        # Store the interaction
        self.previous_interactions.append((question, response))
        return response

    def ask_questions(self):
        if self.questions_asked == 0:
            return "What's your favorite hobby?"
        elif self.questions_asked == 1:
            return "Do you enjoy chatting with bots?"
        elif self.questions_asked == 2:
            return "What would you like to talk about next?"
        else:
            return None

    def recall_context(self):
        if self.previous_interactions:
            last_question, last_response = self.previous_interactions[-1]
            return f"Last we talked about: '{last_question}' - '{last_response}'"
        else:
            return "I don't have any previous context."

    def handle_user_input(self, user_input):
        user_input = user_input.strip().lower()
        if user_input in self.farewell:
            return "Goodbye! Have a great day!"
        
        if self.questions_asked < 3:
            response = self.ask_questions()
            self.questions_asked += 1
            return response
        else:
            # Provide context before answering
            context = self.recall_context()
            response = self.answer_question(user_input)
            return f"{context}\n{response}"

# Create an instance of the SimpleChatbot class
chatbot = SimpleChatbot()

# Start an interactive chat session
print("SimpleBot: Hello! I am SimpleBot. How can I help you today?")

while True:
    user_input = input("You: ").strip()
    response = chatbot.handle_user_input(user_input)
    print(f"SimpleBot: {response}")
    if user_input.lower() in chatbot.farewell:
        break
