import pywhatkit as pt
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyjokes
import pyttsx3
from googletrans import Translator
import wolframalpha

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 120)
r = sr.Recognizer()
lis = ["to", "from", "in", "on"]


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good morning !")
        speak("Good Morning !")
    elif hour >= 12 and hour < 18:
        print("Good Afternoon !")
        speak("Good Afternoon !")
    else:
        print("Good Evening !")
        speak("Good Evening !")


print("I am your dev ")
speak("I am your dev ")


def takeCommand():
    cmd = ''
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            user_voice = r.listen(source)
            print("Recognizing...")
            cmd = (r.recognize_google(user_voice, language='en-in')).lower()
        if 'edith' in cmd or "hey dev" in cmd:
            cmd = cmd.replace("dev ", "")
            cmd = cmd.replace("hey dev ", "")
            print(cmd)
            speak(cmd)
    except Exception as e:
        print("Unable to Recognize your voice.")
    return cmd


while True:
    cmd = takeCommand()
    if 'time' in cmd:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print(current_time)
        speak(current_time)
    elif "wikipedia" in cmd:
        cmd = cmd.replace("wikipedia ", "")
        try:
            result = wikipedia.summary(cmd, sentences=3)
            print(result)
            speak(result)
        except Exception:
            print('no page found on wikipedia')
            speak('no page found on wikipedia')
    elif "play" in cmd or "youtube" in cmd:
        cmd = cmd.replace("play ", "")
        speak("playing" + cmd)
        pt.playonyt(cmd)
    elif "search" in cmd or "search for" in cmd or "search about" in cmd or "search on" in cmd or "tell me about" in cmd:
        cmd = cmd.replace("search ", "")
        cmd = cmd.replace("for ", "")
        cmd = cmd.replace("on ", "")
        cmd = cmd.replace("tell me about ", "")
        speak("searching for " + cmd)
        pt.search(cmd)
    elif "how are you" in cmd:
        print("i am doing good ")
        speak("i am doing good ")
    elif "who created you" in cmd or "who invented you" in cmd:
        print('i am created by Shaheer')
        speak("i am created by Shaheer")
    elif "who are you" in cmd:
        print("i am Shaheer ai assistant")
        speak("i am Shaheer ai assistant")
    elif "open" in cmd or "website" in cmd:
        cmd = cmd.replace("open ", "")
        cmd = cmd.replace("website ", "")
        # url=input("enter the address: ")
        speak("opening the page")
        webbrowser.open("https://" + cmd)
    elif "tell" in cmd and "joke" in cmd:
        my_joke = pyjokes.get_joke(language="en", category="all")
        print(my_joke)
        speak(my_joke)
    elif "how to mix" in cmd:
        print("ask krishna")
        speak("ask krishna")
    elif "what is the meaning of your name" in cmd or "what is the meaning of dev" in cmd:
        print('it means,  Mr.Obothr')
        speak('it means,  Mr.Obothr')
    elif "your name" in cmd:
        print("my name is Dev Dixit")
        speak("my name is Dev Dixit")
    elif "translate" in cmd:
        print(cmd)
        cmd = cmd.replace("translate", "")
        for i in lis:
            if i in cmd:
                cmd = cmd.replace(i + ' ', "")
        cmd = cmd.split()
        print(cmd)
        translator = Translator()
        translation = translator.translate("".join(cmd[:(len(cmd) - 1)]), src='en', dest='te')
        print(translation.text)
    elif "what " in cmd or "where " in cmd or "how " in cmd or "can" in cmd:
        try:
            print(cmd)
            user = wolframalpha.Client('4K484A-JUUA6T27EX')
            res = user.query(cmd)
            answer = next(res.results).text
            print(answer)
            speak(str(answer))
        except Exception:
            print("sorry I'm still learning")
            speak("sorry I'm still learning")
    elif "calculate" in cmd:
        user = wolframalpha.Client('4K484A-JUUA6T27EX')
        print(cmd)
        indx = (cmd.split()).index('calculate')
        query = cmd.split()[indx + 1:]
        res = user.query(' '.join(query))
        answer = next(res.results).text
        print("The answer is " + answer)
        speak("The answer is " + answer)
    elif "good morning" in cmd or "good afternoon" in cmd or "good evening" in cmd:
        wishMe()
    elif "hi" in cmd or "hello" in cmd:
        print("hi,it's really good to hear from you")
        speak("hi,it's really good to hear from you")
    elif "thank you" in cmd:
        print("i am honored to serve")
        speak("i am honored to serve")
    elif "will you be my girl friend" in cmd or "will you be my boy friend" in cmd:
        print("I'm not sure about, may be you should give me some time")
        speak("I'm not sure about, may be you should give me some time")
    elif "i love you" in cmd:
        print("I dont have any feelings  i am chatbot")
        speak("I dont have any feelings  i am chatbot")
    elif "will you marry me" in cmd:
        print('sorry, i am not interested ')
        speak('sorry, i am not interested ')
    elif "close" in cmd or "stop" in cmd:
        print("thanks for using see you later !")
        speak("thanks for using see you later !")
        break
    elif " " in cmd:
        print("Sorry, I can’t help with that yet. I’m still learning.")
        speak("Sorry, I can’t help with that yet. I’m still learning.")