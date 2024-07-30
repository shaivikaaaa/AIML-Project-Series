class AdmissionChatbot:
    def __init__(self) -> None:
        self.previous_interactions = []
        self.admission_info = {
            "application process": "The application process includes submitting an online application form, providing academic transcripts, and taking an entrance exam if required.",
            "requirements": "Requirements include a completed application form, academic transcripts, letters of recommendation, and proof of language proficiency.",
            "deadlines": "Application deadlines are usually June 30th for the Fall semester and November 30th for the Spring semester. Please check the official website for exact dates.",
            "scholarships": "Scholarships are available based on merit and financial need. You can apply for scholarships during the application process.",
            "contact": "For more information, you can contact the admissions office at admissions@college.edu or call (123) 456-7890."
        }
        self.farewell = ["bye", "goodbye", "see you later"]
        self.context = {}

    def answer_question(self, question):
        question = question.lower().strip()
        if question in self.admission_info:
            response = self.admission_info[question]
        else:
            response = "Sorry, I don't have information on that topic. Please visit our website or contact the admissions office for more details."
        # Store the interaction
        self.previous_interactions.append((question, response))
        return response

    def recall_context(self):
        if self.previous_interactions:
            last_question, last_response = self.previous_interactions[-1]
            return f"Last we talked about: '{last_question}' - '{last_response}'"
        else:
            return "I don't have any previous context."

    def engage_user(self):
        if 'admission' in self.context:
            return f"Earlier you mentioned you had questions about admission. How can I assist you further?"
        else:
            return "Feel free to ask me any questions you have about college admissions."

    def handle_user_input(self, user_input):
        user_input = user_input.strip().lower()
        if user_input in self.farewell:
            return "Goodbye! Have a great day!"

        # Update context
        if "admission" in user_input:
            self.context['admission'] = True

        # Provide context before answering
        context = self.recall_context()
        response = self.answer_question(user_input)
        
        # Engagement and personalization
        engagement = self.engage_user()
        return f"{engagement}\n{context}\n{response}" if context else f"{engagement}\n{response}"

# Create an instance of the AdmissionChatbot class
chatbot = AdmissionChatbot()

# Start an interactive chat session
print("AdmissionBot: Hello! I am AdmissionBot. How can I help you with your college admission queries today?")

while True:
    user_input = input("You: ").strip()
    response = chatbot.handle_user_input(user_input)
    print(f"AdmissionBot: {response}")
    if user_input.lower() in chatbot.farewell:
        break
