import pyttsx3 as p
import speech_recognition as sr
from selenium_web import *
from YT_auto import *
from News import *
from jokes import *
from weather import *
import randfacts
import datetime

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def get_date_greeting():
    today_date = datetime.datetime.now()
    greeting = ""
    hour = today_date.hour
    if hour < 12:
        greeting = "Good Morning."
    elif hour < 16:
        greeting = "Good Afternoon."
    else:
        greeting = "Good Evening."

    date_str = today_date.strftime("%d of %B, %I:%M%p")
    return greeting, date_str


def get_user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1)
        print("Listening...")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        return text


def play_song():
    print("Sure. Which song do you want me to play?")
    speak("Sure. Which song do you want me to play?")
    vid = get_user_input()
    print(vid)
    print("Playing {} on YouTube".format(vid))
    speak("Playing {} on YouTube".format(vid))
    assist = music()
    assist.play(vid)


def search_information():
    print("Sure. You need information related to which topic?")
    speak("Sure. You need information related to which topic?")
    info = get_user_input()
    print(info)
    print("Searching {} on Wikipedia".format(info))
    speak("Searching {} on Wikipedia".format(info))
    assist = infow()
    assist.get_info(info)


def read_news():
    print("Sure. Now I will read the news for you.")
    speak("Sure. Now I will read the news for you.")
    arr = news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])


def share_random_fact():
    speak("Sure.")
    fact = randfacts.get_fact()
    print(fact)
    speak("Did you know that " + fact)


def tell_joke():
    arr = joke()
    speak("Get ready for some chuckles.")
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])

def loop():
    print("Anything else you want me to do?")
    speak("Anything else you want me to do?")
    text2 = get_user_input()
    print(text2)
    if "nothing" in text2 or "no" in text2:
        print("Alright. Have a great day!")
        speak("Alright. Have a great day!")
        exit()


def assistant_loop():
    print("Hi, I am your virtual assistant.")
    speak("Hi, I am your virtual assistant.")
    greeting, date_str = get_date_greeting()
    print(greeting)
    speak(greeting)
    print("Today is {}.".format(date_str, date_str))
    speak("Today is {}.".format(date_str, date_str))
    print("The temperature is {} degree Celsius with {}.".format(temp(), des()))
    speak("The temperature is {} degree Celsius with {}.".format(temp(), des()))

    while True:
        print("What can I do for you?")
        speak("What can I do for you?")

        text2 = get_user_input()
        print(text2)

        if "play" and "song" in text2:
            play_song()

        elif "information" in text2:
            search_information()

        elif "news" in text2:
            read_news()

        elif "fact" in text2:
            share_random_fact()

        elif "joke" in text2:
            tell_joke()

        elif "no" in text2 or "nothing" in text2:
            print("Alright. Have a great day!")
            speak("Alright. Have a great day!")
            break

        else:
            print("Sorry. I am not programmed to do that yet.")
            speak("Sorry. I am not programmed to do that yet.")

        loop()


assistant_loop()
