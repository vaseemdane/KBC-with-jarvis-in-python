import random
import pyttsx3
import datetime
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
time=int(datetime.datetime.now().hour)
if time>=0 and time<=12:
    print("good morning")
    speak("good morning")
elif time>12 and time<=5:
    print("good afternoon")
    speak("good afternoon")
else:
    print("good evening")
    speak("good evening")
speak("namaskar deviyo aur sajjano , i am vaseem welcome you all to the kbc show")
speak("so !!!! lets begin the show")
questions= [
    ['What is the capital of Australia?', 'Sydney', 'Melbourne', 'Canberra', 'Brisbane', 3],
    ['Which planet is known as the "Blue Planet"?', 'Mars', 'Earth', 'Neptune', 'Uranus', 2],
    ['What is the smallest prime number?', '0', '1', '2', '3', 3],
    ['In which year did World War II end?', '1943', '1945', '1947', '1950', 2],
    ['Who wrote "The Great Gatsby"?', 'F. Scott Fitzgerald', 'Ernest Hemingway', 'Jane Austen', 'George Orwell', 1],
    ['What is the powerhouse of the cell?', 'Nucleus', 'Mitochondria', 'Ribosome', 'Endoplasmic reticulum', 2],
    ['Which country is known as the Land of Fire and Ice?', 'Italy', 'Iceland', 'New Zealand', 'Canada', 2],
    ['What is the deepest point in the ocean?', 'Mariana Trench', 'Puerto Rico Trench', 'Sargasso Sea', 'Tongue of the Ocean', 1],
    ['Who painted "Starry Night"?', 'Vincent van Gogh', 'Pablo Picasso', 'Claude Monet', 'Leonardo da Vinci', 1],
    ['What is the value of pi (π) to two decimal places?', '3.14', '3.16', '3.18', '3.20', 1],
    ['Which programming language is known for its speed and performance?', 'Python', 'Java', 'C++', 'JavaScript', 3],
    ['What is the chemical symbol for silver?', 'Au', 'Ag', 'Fe', 'Cu', 2],
    ['Who is the author of "1984"?', 'George Orwell', 'Aldous Huxley', 'Ray Bradbury', 'J.K. Rowling', 1],
    ['What is the main ingredient in hummus?', 'Chickpeas', 'Lentils', 'Black beans', 'Quinoa', 1],
    ['In what year did the first manned spaceflight occur?', '1957', '1961', '1969', '1975', 2]
]



levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
for i in range(0,len(questions)):
    que=questions[i]
    print(f"the question for {levels[i]} is \n{que[0]}")
    speak(f"the question for {levels[i]} is \n{que[0]}")
    print(f"1.{que[1]}   2.{que[2]}")
    print(f"3.{que[3]}   4.{que[4]}")
    speak(f"option 1 {que[1]}   option 2 {que[2]}")
    speak(f"option 3 {que[3]}   option 4 {que[4]}")
    ans=(int(input("enter the correct option")))
    speak("think it carefully and tell the answer!!")
    speak(f"your choosen answer is {ans}")

    if (ans==que[5]):
        print(f"you have won {levels[i]} rupees")
        speak(f"you have won {levels[i]} rupees")
    else:
        print('better luck next time')
        speak('better luck next time')
        print(f"your total earning is {levels[i]}")
        speak(f"your total earning is {levels[i]}")
        exit()
# print(f"game over meet you next week , and your total winnings is {levels[i]}")