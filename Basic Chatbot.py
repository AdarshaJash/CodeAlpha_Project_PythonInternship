import nltk
from nltk.chat.util import Chat, reflections
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
pairs = [
    [
        r"my name is (.*)",
        ["Hello , How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created by ADARSHA JASH.  You can call me your Chatbot.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good \n How about You?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright","It's OK, no problem",]
    ],
    [
        r"I am (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great!",]
    ],
    [
        r"quit",
        ["Bye for now. Have a great day!","Goodbye!"]
    ],
    [
        r"(.*)",
        [ "Sorry! I could not understand, I am still learning"]
    ],
]
reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}
chatbot = Chat(pairs, reflections)
def chatbot_conversation():
    print("Hi, I'm a chatbot created by ADARSHA JASH.  Let's have a conversation!  Type 'quit' to exit.")
    while True:
        user_input = input("> ")
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(response)
if __name__ == "__main__":
    chatbot_conversation()