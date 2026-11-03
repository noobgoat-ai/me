
# while True:

#     msg = input("You: ").lower()

#     if msg == "hello" or msg == "hi":
#         print("Bot: Hello!")

#     elif msg == "name":
#         print("Bot: I am a chatbot.")

#     elif msg == "how are you":
#         print("Bot: I am fine!")

#     elif msg == "help":
#         print("Bot: How can I help you?")

#     elif msg == "thanks":
#         print("Bot: Welcome!")

#     elif msg == "bye":
#         print("Bot: Goodbye!")
#         break

#     else:
#         print("Bot: Sorry, I don't understand.")



print("Chatbot: Hello! Welcome to my chatbot.")
print("Type 'bye' to exit.")

while True:

    user = input("You: ").lower()

    if "hello" in user or "hi" in user or "hey" in user:
        print("Bot: Hello! How can I help you?")

    elif "name" in user:
        print("Bot: I am a simple AI chatbot.")

    elif "how are you" in user:
        print("Bot: I am fine. Thank you for asking!")

    elif "course" in user or "subject" in user:
        print("Bot: I can provide basic information about your course.")

    elif "help" in user:
        print("Bot: You can ask me about my name or course.")

    elif "thank" in user:
        print("Bot: You are welcome!")

    elif "bye" in user or "exit" in user or "quit" in user:
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I do not understand your question.")
