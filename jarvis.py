import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import random, string
import pyjokes

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)
    


def wishme():
    speak("Welcome back sir!")
    # time()
    # date()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour < 12:
        speak("Good morning Sir!")
    elif hour >=12 and hour < 16:
        speak("Good Afternoon Sir!")
    elif hour >=16 and hour <20:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")

    speak("Jarvis at your service. Please tell me how can i help you?")



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recongnizning...")
        query = r.recognize_google(audio, language="en-in")
        print(query)
    
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    
    return query



#wishme()
#time()
#date()
#takeCommand()


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sandeepmoditest@gmail.com', 'leidwgzsahhqoacm')
    server.sendmail('sandeepmoditest@gmail.com', to, content)
    server.close()



def mailAccount():
    speak("Tell me the gmail account..")
    to = takeCommand().lower()
    to = to.replace('at the rate','@')
    to = to.replace(' ','')
    print(to)
    return to


def mailMsg():
    speak("What should i say?")
    content = takeCommand()
    return content


def screenshot():
    try:
        img = pyautogui.screenshot()
        # img.save()
        # global pics_names
    
        def generate_name():
            return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
        
        name = str(generate_name())
        # pics_names.append(name)
        img.save("D:\\PRJ\\AI_ML_Prj\\Jarvis\\"+ name + '.jpg')
        speak("Screenshot Done!")
    except:
        speak("unable to take screenshot.")


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+ usage)
    battery = psutil.sensors_battery()
    speak("Batteryis at")
    speak(battery.percent)


def jokes():
    speak(pyjokes.get_joke(language='en'))


if __name__ == "__main__":
    speak("Hello, this is JARVIS AI Assistant.")
    #wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()


        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query, sentences = 3)
            print(result)
            speak(result)


        elif 'send email' in query:
            try:
                to = mailAccount()
                content = mailMsg()
                sendEmail(to,content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Unable to send the email")


        elif 'search in chrome' in query:
            speak("What should i search?")
            # chromepath = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
            chromepath = 'C:\Program Files\Internet Explorer\iexplore.exe'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search)


        elif 'logout' in query:
            os.system("shutdown -l")
        # elif 'shutdown' in query:
        #     os.system("shutdown /s /t l")
        # elif 'restart' in query:
        #     os.system("shutdown /r /t l")


        elif 'play music' in query:
            songs_dir = 'D:\\Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        # elif 'music off' in query:


        elif 'remember that' in query:
            speak("What should i remember?")
            data = takeCommand()
            speak("you said me to remember " + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()


        elif 'do you know anything' in query:
            remember = open("data.txt", 'r')
            speak("you said me to remember that" + remember.read())


        elif 'screenshot' in query:
            screenshot()
            
        elif 'cpu' in query:
            cpu()
        
        elif 'joke' in query:
            jokes()

        elif 'jarvis off' in query:
            speak("Jarvis off")
            quit()
            