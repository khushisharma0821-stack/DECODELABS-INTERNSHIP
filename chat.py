print("🤖 Rule-Based AI Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ")

    if user.lower() == "hi":
        print("Bot: Hello! Nice to meet you.")

    elif user.lower() == "hello":
        print("Bot: Hi there!")

    elif user.lower() == "how are you":
        print("Bot: I am fine. Thank you!")

    elif user.lower() == "what is your name":
        print("Bot: I am a Rule-Based AI Chatbot.")

    elif user.lower() == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")
        