# Simple Chatbot
responses = {"hi": "Hello!", "how are you": "I'm fine, thanks!", "bye": "Goodbye!"}
while (user_input := input("You: ").lower()) != "bye":
    print("Bot:", responses.get(user_input, "I don't understand."))
