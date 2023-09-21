import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Initialize the lemmatizer and stop words
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Define the chatbot's responses
responses = {
    "hello": ["Hi there! How can I assist you today?"],
    "how are you": ["I'm doing well, thank you for asking! How can I help you today?"],
    "what is your name": ["My name is LLaMA, I'm a large language model trained by a team of researcher at Meta AI."],
    "who are you": ["I am LLaMA, a chatbot developed by Meta AI."],
    "where are you from": ["I am a computer program, so I don't have a physical location."],
    "what can you do": ["I can answer questions and provide information on a wide range of topics. I can also generate text based on prompts and complete tasks such as writing emails or summarizing articles."],
    "goodbye": ["Goodbye! It was nice chatting with you. Is there anything else I can help you with?"]
}

# Define the chatbot's conversation flow
def chat():
    # Initialize the conversation
    print("Hello! I'm LLaMA, a chatbot developed by Meta AI.")
    user_input = input("What can I help you with today?\n")

    # Process the user's input
    tokens = word_tokenize(user_input)
    tokens = [word.lower() for word in tokens]
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    tokens = [word for word in tokens if word not in stop_words]

    # Generate the response
    response = ""
    for token in tokens:
        if token in responses:
            response += responses[token][0] + "\n"
        else:
            response += "I don't understand what you mean by '" + token + "'."

    # Print the response
    print(response)

# Start the conversation
chat()
