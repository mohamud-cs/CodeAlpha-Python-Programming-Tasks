name = input("What is your name? ")
print("Hello, " + name + "! Welcome to the chatbot.")
print("You can ask me anything, and I'll try to answer.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye! It was nice talking to you.")
        break
    else:
        print("Chatbot: I'm sorry, I don't have an answer for that yet.")   