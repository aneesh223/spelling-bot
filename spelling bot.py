import random, pyttsx3
from list_maker import parsedlst as wordlist

def bot(list_):
    engine = pyttsx3.init()
    print("welcome to the spelling bot! type /quit to quit")
    while True:  
        word = random.choice(list_)
        while True:    
            engine.say (f"Your word is: {word}")
            engine.runAndWait()
            input_ = input("Answer: ")
            if input_ == word:
                print("Correct!")
                engine.say ("Correct")
                engine.runAndWait()
                break
            elif input_ == "/quit":
                quit()
            elif input_ == "/repeat":
                pass
            else:
                spelling = " ".join(word)
                print(f"Incorrect: the answer is {word}")
                engine.say("Incorrect: the answer is")
                engine.say(spelling)
                engine.runAndWait()
                break
        


if __name__ == '__main__':
    bot(wordlist)