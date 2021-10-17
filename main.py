import datetime

import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia

#works only with windows and linux

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say('I am crazy f')
    engine.say('you can talk to me')
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening Faiz...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'crazy' in command:
                command = command.replace('crazy', '')
                print(command)
    except:
        pass


    return (command)


def run_alexa():
    
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        print(song)
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('Current time is ' + time)

    elif 'todays date' in command:
        date = datetime.datetime.now().strftime('%I:%M %p')
        print(datetime.date)
        talk('Todays Date is ' + date)

    elif 'what is ' in command:
        search = command.replace('what is', '')
        info = wikipedia.summary(search, 1)
        print(info)
        talk(info)

    elif 'who is ' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'where is ' in command:
        place = command.replace('where is', '')
        info = wikipedia.summary(place, 1)
        print(info)
        talk(info)

    elif 'date' in command:
        talk('sorry, I have a headache')

    elif 'are you single' in command:
        talk('I am in a relationship with wifi')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk('Could you please repeat that for me .')


while True:
    
    run_alexa

else:
    pass
