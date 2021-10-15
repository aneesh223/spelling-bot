import random, pyttsx3
from list_maker import parsedlst

def bot(list_):
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')[0]
    engine.setProperty('voice',voice.id)
    print("welcome to the spelling bot! type /q to stop the bot, or /r to repeat the word")
    while True:
        word = random.choice(list_)
        while True:
            engine.say (f"Your word is: {word}")
            engine.runAndWait()
            input_ = input("")
            if input_ == word:
                print("Correct!")
                engine.say ("Correct")
                engine.runAndWait()
                break
            elif input_ == "/q":
                quit()
            elif input_ == "/r":
                pass
            else:
                spelling = " ".join(word)
                print(f"Incorrect: the answer is {word}")
                engine.say("Incorrect: the answer is")
                engine.say(spelling)
                engine.runAndWait()
                break



if __name__ == '__main__':
    bot(parsedlst)