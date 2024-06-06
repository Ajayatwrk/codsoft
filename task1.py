def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm here to help you!"
    elif "your name" in user_input:
        return "I am a simple rule-based chatbot created to assist you."
    elif "help" in user_input:
        return "Sure, I'm here to help! What do you need assistance with?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

# Testing the chatbot
print(chatbot_response("Hello"))
print(chatbot_response("How are you?"))
print(chatbot_response("What is your name?"))
print(chatbot_response("Can you help me?"))
print(chatbot_response("Goodbye"))
