import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

#listener = sr.Recognizer()
engine= pyttsx3.init()
voices =engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say('I am alexa, what can i do for you')
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening........")
            command = input("say something:")
            engine.say(command)
            engine.runAndWait()
            #voice = listener.listen(source)
           # command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command
def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
         song=command.replace('play','')
         pywhatkit.playonyt(command)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%H:%M')
        print(time)
        imp = datetime.datetime.now().strftime('%I:%M')
        talk('The time in hours is '+time)
        print(imp)
        talk("the time in 12 format is"+ imp)
    elif 'day' in command:
        #date = datetime.datetime.now().date()
        date = datetime.datetime.today()

        print(date)
        talk(date)
    elif 'who' in command:
        person = command.replace('who is ','')
        info =wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'are you single' in command:
        talk("I am in a relationship with wifi")
    #elif 'date' in command:
        #talk('i have a headache')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'what' in command:
        pywhatkit.search(command)
        per = command.replace('what is ', '')
        val = wikipedia.summary(per, 1)
        print(val)
        talk(val)

    elif 'how' in command:
        pywhatkit.search(command)
        result = command.replace('how ', '')
        value = wikipedia.summary(result, 1)
        talk(value)

    else:
        pywhatkit.search(command)
        result = command
        #response =pywhatkit.info(result)
        value = wikipedia.summary(result, 1)
        print(value)
        talk(value)
        #talk(response)

    #else:
     #  talk('please say the command again.')



    print("searching...")
while True:
     run_alexa()
