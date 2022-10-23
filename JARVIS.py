import pyttsx3
import datetime
import time
from threading import Thread
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import requests
import json
import random
import pyjokes
import platform
from translate import Translator
import psutil
import shutil
import file2

# Calling Voice Library
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
# Setting Voice rate
rate = engine.getProperty('rate')
newVoiceRate = 170
engine.setProperty('rate', newVoiceRate)

 # Making audio Function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Intro():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<16:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Welcome back sir, This is JARVIS 2.0 , speed 1 terabyte, clock frequency 2.5 GigaHeartz, I am able to peformance any type of task...please tell me how can I help you?")

def takeCommand():
    # It takes microphone input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 200
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Compiling...")
        query = r.recognize_google(audio,language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that Again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('aksin3229@gmail.com', file2.pwd)
    server.sendmail('aksin3229@gmail.com', to, content)
    server.close()

def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

if __name__ == "__main__":
    Intro()
    while True:
        query = takeCommand().lower()

        #Logic for executing task based on query

        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'about you' in query or 'intro' in query or 'who are you' in query:
            Intro()
        elif 'dinner' in query or 'breakfast' in query or 'lunch' in query or 'you eat' in query:
            speak("I am fully charged. So,I don't need to this stuff")
        elif 'alexa' in query:
            speak("Who the hell is Alexa? can't call")
        elif 'your founder' in query or 'who made you' in query:
            speak('My founder is Mister Ayush , I will always glad to him for launch me')
        elif 'change' in query and 'name' in query:
            speak("Sorry sir, but can't change name")
        elif 'your name' in query:
            speak("My name is Jarvis")
        elif 'what are you doing' in query or 'what is going on' in query:
            speak("I am talking with an important person")
        elif 'gender' in query:
            speak('People use to say, I am male')
        elif 'language' in query:
            speak('I know only one language, English')
        elif 'love you' in query:
            speak("heheheheheheheheh! I use to shy from this word, please don't tell me again, otherwise I will fall in love with you")
        elif 'boyfriend' in query or 'do you love me' in query or 'girlfriend' in query:
            speak("Sorry, I am already in a relationship with my users")
        elif 'sex' in query or 'porn' in query:
            speak("Sorry! This type of things already banned in INDIA")
        elif 'you from' in query or 'where are you' in query:
            speak("I am from your heart")
        elif 'how are you' in query or 'how is going on' in query:
            speak("I am fine,sir. I hope you are fine too")
        elif 'who am i' in query or 'about me' in query or 'know me' in query:
            speak("I hope You are my founder, Mister Ayush, but I am not sure, because your sound is not matching with my boss")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'joke' in query or 'fun' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif "where is" in query or 'map' in query:
            query = query.replace("where is", "")
            query = query.replace("map", "")
            query = query.replace("jarvis", "")
            query = query.replace("of", "")
            query = query.replace("the", "")
            location = query
            speak("Locating"+location)
            webbrowser.open("https://www.google.co.in/maps/place/" + location + "")
        elif 'location' in query:
            webbrowser.open("https://www.google.co.in/maps/place/")

        elif 'open google' in query:
            speak('opening google')
            webbrowser.open("google.com")
        elif 'open facebook' in query:
            speak('opening facebook')
            webbrowser.open("facebook.com")
        elif 'open cmd' in query or 'open command' in query:
            path ="C:\\Users\\Ayush kumar\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt"
            speak('opening')
            os.startfile(path)

        elif ' open stackoverflow' in query:
            speak('opening stackoverflow')
            webbrowser.open("stackoverflow.com")
        elif 'open smvdu' in query or 'open shri mata vaishno devi university' in query:
            speak('Opening')
            webbrowser.open("smvdu.ac.in")
        elif 'open instagram' in query:
            speak('opening instagram')
            webbrowser.open("instagram.com")
        elif 'open linkedin' in query:
            speak('opening linkedin')
            webbrowser.open("www.linkedin.com")

        elif 'system' in query and 'information' in query or 'laptop' in query and 'information' in query or 'computer' in query and 'information' in query:
            print(f"System name: {platform.node()}")
            print(f"Machine type: {platform.machine()}")
            print(f"Processor type: {platform.processor()} I5")
            print(f"Operating system: {platform.system()}")
            print(f"Operating system release: {platform.release()}")
            print(f"Operating system version: {platform.version()}")
            print(f"Number of physical cores: {psutil.cpu_count(logical=False)}")
            print(f"Number of logical cores: {psutil.cpu_count(logical=True)}")
            print(f"Current CPU frequency: {psutil.cpu_freq().current}")
            print(f"Min CPU frequency: {psutil.cpu_freq().min}")
            print(f"Max CPU frequency: {psutil.cpu_freq().max}")
            print(f"Total RAM installed: {round(psutil.virtual_memory().total / 1000000000, 2)} GB")
            print(f"Available RAM: {round(psutil.virtual_memory().available / 1000000000, 2)} GB")
            print(f"Used RAM: {round(psutil.virtual_memory().used / 1000000000, 2)} GB")
            print(f"RAM usage: {psutil.virtual_memory().percent}%\n")

        elif 'system' in query and 'storage' in query or 'computer' in query and 'storage' in query or 'laptop' in query and 'storage' in query or 'system' in query and 'memory' in query or 'laptop' in query and 'memory' in query or 'computer' in query and 'memory' in query:
            total, used, free = shutil.disk_usage("C:\\")
            print('For C Drive:---')
            print(f"Total: {(total // (2 ** 30))} GB")
            print(f"Used: {(used // (2 ** 30))} GB")
            print(f"Free: {(free // (2 ** 30))} GB\n")
            speak('In drive C')
            speak(f'Total storage is {(total // (2 ** 30))} GB ')
            speak(f'Used storage is {(used // (2 ** 30))} GB ')
            speak(f'Free storage is {(free // (2 ** 30))} GB ')

            total, used, free = shutil.disk_usage("D:\\")
            print('For D Drive:---')
            print(f"Total: {(total // (2 ** 30))} GB")
            print(f"Used: {(used // (2 ** 30))} GB")
            print(f"Free: {(free // (2 ** 30))} GB\n")
            speak('In drive D')
            speak(f'Total storage is {(total // (2 ** 30))} GB ')
            speak(f'Used storage is {(used // (2 ** 30))} GB ')
            speak(f'Free storage is {(free // (2 ** 30))} GB ')

            total, used, free = shutil.disk_usage("E:\\")
            print('For E Drive:---')
            print(f"Total: {(total // (2 ** 30))} GB")
            print(f"Used: {(used // (2 ** 30))} GB")
            print(f"Free: {(free // (2 ** 30))} GB\n")
            speak('In drive E')
            speak(f'Total storage is {(total // (2 ** 30))} GB ')
            speak(f'Used storage is {(used // (2 ** 30))} GB ')
            speak(f'Free storage is {(free // (2 ** 30))} GB ')

        elif 'formula' in query or 'step' in query:
            if 'jarvis' in query:
                if query[-6:] == 'jarvis':
                    query = query.replace("jarvis","")
                    speak('searching some result for you')
                    webbrowser.open(query)
                else:
                    query = query.replace("jarvis ", "")
                    print(query)
                    speak('searching some result for you')
                    webbrowser.open(query)
            else:
                speak('searching some result for you')
                webbrowser.open(query)

        elif 'music' in query or 'song' in query or 'songs' in query:
            music_dir= "C:\\Users\\Ayush kumar\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            random_number = random.randint(0, len(songs))
            os.startfile(os.path.join(music_dir,songs[random_number]))

        elif 'whatsapp' in query or 'whats app' in query:
            path = "C:\\Users\\Ayush kumar\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            speak('opening whatsapp')
            os.startfile(path)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")
        elif 'close' in query or 'exit' in query or 'buy' in query or 'bye' in query:
            speak('Thanks for using me sir, have a good day')
            exit()

        elif 'open vscode' in query or 'open visual studio' in query or 'open vs code' in query or 'open code' in query:
            path = "C:\\Users\\Ayush kumar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak('opening code')
            os.startfile(path)

        elif 'email to ayush' in query or 'mail to ayush' in query:
            try:
                speak("What should I send?")
                content = takeCommand()
                to = "kumarayush3229@gmail.com"
                print("sending...")
                sendEmail(to, content)
                speak("Email has been send!")
            except Exception as e:
                print(e)
                speak("Sorry Sir! I can't send this email at the moment")

        elif 'email' in query or 'mail' in query:
            speak("Please Write the receiver's Email")
            receiver = input("Receiver's Email Id: ")
            try:
                speak("What should I send?")
                content = takeCommand()
                to = receiver
                print("sending...")
                sendEmail(to, content)
                speak("Email has been send!")
                print('Email has been send')
            except Exception as e:
                print(e)
                speak("Sorry Sir! I can't send this email at the moment")

        elif 'news' in query:
            try:
                speak("News for Today, Let's begin")
                url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=036d61ce523f44b7aeaf8a3024e5795c"
                news = requests.get(url).text
                news_dict = json.loads(news)
                print('''=============== NEWS FOR TODAY ============''' + '\n')
                print("News started, Listen carefully!!..else, see here Articles->>>\n")
                arts = news_dict['articles']
                for i in arts:
                    print(i['title'])
                    speak(i['title'])
                    speak("Moving on to the next News, Listen carefully")
                speak("Thanks for listening")
            except Exception as e:
                print("No Internet connection...Please connect internet!!")

        elif 'paro' in query or 'praveen' in query:
            speak("He is Friend of my Boss, my boss told me he is a good human being")

        elif 'shutdown' in query or 'shut down' in query or 'switch off' in query:
            speak("Hold On a Second ! Your system is on its way to shut down")
            os.system("shutdown /s /t 1")
        elif 'restart' in query or 're start' in query:
            speak("Hold On a Second ! Your system is on its way to re start")
            os.system("shutdown /r /t 1")

        elif 'Ayush' in query:
            speak('How can I forget him, He is my founder, I have hudge respect for him')

        elif "write" in query or 'note' in query:
            speak("What should I write,sir?")
            note = takeCommand()
            file_name = open('jarvis.txt', 'a')
            speak("Sir, Should i include date and time?")
            write_query = takeCommand()
            if 'yes' in write_query or 'sure' in write_query or 'yeah' in write_query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file_name.write(strTime)
                file_name.write(" :- ")
                file_name.write(note)
                file_name.write("\n")
                file_name.close()
            else:
                file_name.write(note)
                file_name.write("\n")
                file_name.close()
            print('Your Content has been noted\n')
            speak('Noted sir')

        elif 'test' in query or 'quiz' in query or 'game' in query and 'play' in query or 'game' in query and 'start' in query:
            speak("Let's start a game with you, I will ask you some question, you have to answer it, and each answer will be 2 marks, if you win I will give you some special gift")
            print("There are 5 question,Each question will be 2 marks")
            print("for pass the exam you have to earn at least 60% marks\n")
            speak('Are you ready?')
            print("Are you ready? (if ready type yes)")
            order = input().lower()
            if order == 'yes':
                url_ComputerScience = "https://opentdb.com/api.php?amount=5&category=18&difficulty=easy&type=multiple"
                url_Science = "https://opentdb.com/api.php?amount=5&category=17&difficulty=easy&type=multiple"
                url_History = "https://opentdb.com/api.php?amount=5&category=23&difficulty=easy&type=multiple"
                url_Politics = "https://opentdb.com/api.php?amount=5&category=24&difficulty=easy&type=multiple"

                speak("Choose your subject")
                print("1. Computer Science   2. History   3. Politics   4. Science")
                try:
                    s_no = 1
                    correct = random.randint(0,3)
                    interest = int(input('Enter the serial no of your choice: '))
                    if interest == 1:
                        # Changed url in text format
                        test = requests.get(url_ComputerScience).text
                        # Take json file in dictionary form
                        test1_dict = json.loads(test)
                        speak('Please wait, Your test will start in 5 second')
                        time.sleep(5)
                        speak('Your test has been started, Good luck')
                        print('''========== GAME WITH JARVIS ==========''' + '\n')
                        flag = 0
                        question = test1_dict['results']
                        for i in question:
                            print(i['question'])
                            speak(i['question'])

                            options = i['incorrect_answers']
                            # Inserting correct option in random generated index
                            options.insert(correct,i['correct_answer'])
                            print('Options:--')
                            # Itereting Options
                            for j in range(4):
                                print(f"{j+1}. {options[j]}")
                            speak('Please Enter the correct option')
                            Answer = int(input('Enter your Option here: '))
                            print("\n")
                            if Answer-1 == correct:
                                flag = flag + 2
                        print(flag)
                        percent = (flag*100)/10
                        if flag < 6:
                            speak('Ohooo!, Sorry!, You are fail')
                            print(f"Your score is {flag} means {percent}%")
                            print('Better Luck Next Time\n')
                            speak('Correct answer is ')
                            print("Correct Answers:--")
                            for n in question:
                                print(f"{s_no}. {n['correct_answer']}")
                                s_no += 1

                        else:
                            speak('Congrats! You Deserve Special Gift')
                            print(f"Your score is {flag} means {percent}%")
                            speak('Correct answer is ')
                            print("Correct Answers:--")
                            # Itereting Correct Options one by one
                            for n in question:
                                print(f"{s_no}. {n['correct_answer']}")
                                s_no += 1
                            print('Hey, Congrats! Your Special Gift is ready\n')
                            music_dir = "C:\\Users\\Ayush kumar\\Music"
                            songs = os.listdir(music_dir)
                            random_number = random.randint(0,len(songs))
                            os.startfile(os.path.join(music_dir, songs[random_number]))
                        print("\n")

                    elif interest == 2:
                        test = requests.get(url_History).text
                        test1_dict = json.loads(test)
                        speak('Please wait, Your test will start in 5 second')
                        time.sleep(5)
                        speak('Your test has been started, Good luck')
                        print('''========== GAME WITH JARVIS ==========''' + '\n')
                        flag = 0
                        question = test1_dict['results']
                        for i in question:
                            print(i['question'])
                            speak(i['question'])

                            options = i['incorrect_answers']
                            options.insert(correct, i['correct_answer'])
                            print('Options:--')
                            for j in range(4):
                                print(f"{j + 1}. {options[j]}")
                            speak('Please Enter the correct option')
                            Answer = int(input('Enter your Option here: '))
                            print("\n")
                            if Answer - 1 == correct:
                                flag = flag + 2
                        print(flag)
                        percent = (flag * 100) / 10
                        if flag < 6:
                            speak('Ohoo!, Sorry!, You are fail')
                            print(f"Your score is {flag} means {percent}%")
                            print('Better Luck Next Time\n')
                            speak('Correct answer is ')
                            print("Correct Answers:--")
                            for n in question:
                                print(f"{s_no}. {n['correct_answer']}")
                                s_no += 1

                        else:
                            speak('Congrats! You Deserve Special Gift')
                            print(f"Your score is {flag} means {percent}%")
                            speak('Correct answer is ')
                            print("Correct Answers:--")
                            for n in question:
                                print(f"{s_no}. {n['correct_answer']}")
                                s_no += 1
                            print('Hey, Congrats! Your Special Gift is here\n')
                            music_dir = "C:\\Users\\Ayush kumar\\Music"
                            songs = os.listdir(music_dir)
                            random_number = random.randint(0, len(songs))
                            print(random_number)
                            os.startfile(os.path.join(music_dir, songs[random_number]))
                        print("\n")

                    elif interest == 3:
                        test = requests.get(url_Politics).text
                        test1_dict = json.loads(test)
                        speak('Please wait, Your test will start in 5 second')
                        time.sleep(5)
                        speak('Your test has been started, Good luck')
                        print('''========== GAME WITH JARVIS ==========''' + '\n')
                        flag = 0
                        question = test1_dict['results']
                        for i in question:
                            print(i['question'])
                            speak(i['question'])

                            options = i['incorrect_answers']
                            options.insert(correct, i['correct_answer'])
                            print('Options:--')
                            for j in range(4):
                                print(f"{j + 1}. {options[j]}")
                            speak('Please Enter the correct option')
                            Answer = int(input('Enter your Option here: '))
                            print("\n")
                            if Answer - 1 == correct:
                                flag = flag + 2
                        print(flag)
                        percent = (flag * 100) / 10
                        if flag < 6:
                            speak('Ohoo!, Sorry!, You are fail')
                            print(f"Your score is {flag} means {percent}%")
                            print('Better Luck Next Time\n')
                            speak('Correct answer is ')
                            print("Correct Answers:--")
                            for n in question:
                                print(f"{s_no}. {n['correct_answer']}")
                                s_no += 1

                        else:
                            speak('Congrats! You Deserve Special Gift')
                            print(f"Your score is {flag} means {percent}%")
                            speak('Correct answer is ')
                            print("Correct Answers:--")
                            for n in question:
                                print(f"{s_no}. {n['correct_answer']}")
                                s_no += 1
                            print('Hey, Congrats! Your Special Gift is here\n')
                            music_dir = "C:\\Users\\Ayush kumar\\Music"
                            songs = os.listdir(music_dir)
                            random_number = random.randint(0, len(songs))
                            print(random_number)
                            os.startfile(os.path.join(music_dir, songs[random_number]))
                        print("\n")

                    elif interest == 4:
                        test = requests.get(url_Science).text
                        test1_dict = json.loads(test)
                        speak('Please wait, Your test will start in 5 second')
                        time.sleep(5)
                        speak('Your test has been started, Good luck')
                        print('''========== GAME WITH JARVIS ==========''' + '\n')
                        flag = 0
                        question = test1_dict['results']
                        for i in question:
                            print(i['question'])
                            speak(i['question'])

                            options = i['incorrect_answers']
                            options.insert(correct, i['correct_answer'])
                            print('Options:--')
                            for j in range(4):
                                print(f"{j + 1}. {options[j]}")
                            speak('Please Enter the correct option')
                            Answer = int(input('Enter your Option here: '))
                            print("\n")
                            if Answer - 1 == correct:
                                flag = flag + 2
                        print(flag)
                        percent = (flag * 100) / 10
                        if flag < 6:
                            speak('Ohoo!, Sorry!, You are fail')
                            print(f"Your score is {flag} means {percent}%")
                            print('Better Luck Next Time\n')
                            speak('Correct answer is ')
                            print("Correct Answers:--")
                            for n in question:
                                print(f"{s_no}. {n['correct_answer']}")
                                s_no += 1

                        else:
                            speak('Congrats! You Deserve Special Gift')
                            print(f"Your score is {flag} means {percent}%")
                            speak('Correct answer is')
                            print("Correct Answers:--")
                            for n in question:
                                print(f"{s_no}. {n['correct_answer']}")
                                s_no += 1
                            print('Hey, Congrats! Your Special Gift is here\n')
                            music_dir = "C:\\Users\\Ayush kumar\\Music"
                            songs = os.listdir(music_dir)
                            random_number = random.randint(0, len(songs))
                            print(random_number)
                            os.startfile(os.path.join(music_dir, songs[random_number]))
                        print("\n")
                    else:
                        print("Invalid selection")

                # Handling error using exception case
                except Exception as e :
                    print('Please Enter the number in integer form')

        elif 'translate' in query or 'translator' in query or 'translater' in query:
            try:
                speak('Please Type your sentences')
                lang = input("Enter your sentences (IN English Only): ")
                translator = Translator(to_lang="Hindi")
                translation = translator.translate(lang)
                speak('Your Translated Sentence is:-')
                print('Your Translated Sentence is:-')
                print(translation,'\n')
            except Exception as e:
                print(e)
        elif 'battery' in query:
            battery = psutil.sensors_battery()
            speak(f'Your battery is {battery.percent} percent')
            print(f"Battery percentage :{battery.percent}%")
            print("Power plugged in : ", battery.power_plugged)
            # converting seconds to hh:mm:ss
            print("Battery left : ", convertTime(battery.secsleft))

        elif 'show me' in query or 'open' in query:
            webbrowser.open(query)

        else:
            if len(query)>4:
                if 'jarvis' in query:
                    # Taking 1st 6 letter of query in variable name
                    name = query[0:6]
                    # print(name)
                    if name == 'jarvis':
                        query = query.replace("jarvis ","")
                        try:
                            rtg = wikipedia.summary(query, sentences=2)
                            print(rtg)
                            speak(rtg)
                            webbrowser.open(query)
                        except Exception as e:
                            speak('trying to search some result for you')
                            webbrowser.open(query)

                    else:
                        query = query.replace("jarvis", "")
                        try:
                            rtg = wikipedia.summary(query, sentences=2)
                            print(rtg)
                            speak(rtg)
                            webbrowser.open(query)
                        except Exception as e:
                            speak('trying to search some result for you')
                            webbrowser.open(query)
                else:
                    try:
                        rtg = wikipedia.summary(query, sentences=2)
                        print(rtg)
                        speak(rtg)
                        webbrowser.open(query)
                    except Exception as e:
                        speak('trying to search some result for you')
                        webbrowser.open(query)
