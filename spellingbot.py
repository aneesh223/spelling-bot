import random, pyttsx3
from list_maker import parsedlst

def askword(engine, list_):    
    word = random.choice(list_)
    engine.say (f"Your word is: {word}")
    engine.runAndWait()

def checkword(engine, input_, word):
    if input_ == word:
        print("Correct!")
        engine.say ("Correct")
        engine.runAndWait()
    else:
        spelling = " ".join(word)
        print(f"Incorrect: the answer is {word}")
        engine.say("Incorrect: the answer is")
        engine.say(spelling)
        engine.runAndWait()
