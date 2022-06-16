# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import os
import speech_recognition as sr
from gtts import gTTS
import datetime
import warnings
import calendar
import random
from random import randint
import wikipedia

warnings.filterwarnings('ignore')

def recordAudio():
    # Use a breakpoint in the code line below to debug your script.
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)

    data = ''
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Unknown error")
    except sr.RequestError as e:
        print("Request results could not be made")

    return data

def assistantResponse(text):
    print(text)
    myobj = gTTS(text=text, lang='en', slow=False)
    myobj.save('HCBBB.mp3')
    os.system('HCBBB.mp3')

def wakeupWord(text):

    WAKE_WORDS = ['okay computer', 'okay stella', 'hello computer']
    text = text.lower()
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
    # If not in list, return False
    return False

def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    month_names = ["January","February","March","April","May","June","July",
            "August","September","October","November","December"]

    ordinalNumbers = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th",
    "10th","11th","12th","13th","14th","15th","16th","17th","18th","19th","20th",
    "21st","22nd","23rd","24th","25th","26th","27th","28th","29th","30th","31st"]

    return f"Today is {weekday}, {month_names[monthNum - 1]} {ordinalNumbers[dayNum - 1]}."

def greeting(text):

    #sample greeting inputs
    GREETING_INPUT = ["Hey there", "Hello", "Hi you"]
    GREETING_RESPONSE = ["hello", "hey there", "What is cracking boss", "Yo yo yo", "what is good", "how is it going"]

    for word in text.split():
        if word.lower() in GREETING_INPUT:
            return random.choice(GREETING_RESPONSE)

    return ''

def giveJokes():
    j = open(".\jokes.json")
    laugh = json.load(j)

    questions = laugh["jokes"]
    random_index = randint(0, len(questions)-1)

    setup=questions[random_index]['setup']
    punchline=questions[random_index]['punchline']

    return f"I've got a joke: {setup} ... {punchline}"


def motivation():
    f = open(".\quotes.json")
    quote = json.load(f)

    questions = quote["motivation"]
    random_index = randint(0, len(questions)-1)

    total_line = f"You know, {questions[random_index]['author']} once said {questions[random_index]['text']}. And I think that hit's home for you"

    return total_line

    # return random.choice(quote)

def giveFlattery():
    a_file = open(".\pickuplines.txt", encoding="utf8")
    file_contents = a_file.read()
    contents_split = file_contents.splitlines()

    return random.choice(contents_split)

while True:
    #Record recordAudio
    text = recordAudio()
    response = ''

    if(wakeupWord(text) == True):
        print("You said the wake word, starting up assistant")
        #Check for greetings
        response = response + greeting(text)
        #Check for date
        if('date' in text):
            get_date = getDate()
            response = response + ' ' + get_date

        if('joke' in text):
            get_joke = giveJokes()
            response = response + ' ' + str(get_joke)

        if('line' in text):
            get_hit = giveFlattery()
            response = response + ' ' + str(get_hit)

        if('motivation' in text):
            get_motivation = motivation()
            response = response + ' ' + get_motivation

        assistantResponse(response)
        #assistantResponse(response)

# print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

#if __name__ == '__main__':
 #   print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
