import datetime
import os
import win32com.client
import speech_recognition as sr
import webbrowser
import requests
import random
import threading
import time

speaker = win32com.client.Dispatch("SAPI.SpVoice")

# Global variable to track whether Jarvis is sleeping
jarvis_sleeping = False

# Function to fetch news using News API
def fetch_news():
    news_base_url = "https://newsapi.org/v2/top-headlines"
    news_params = {
        "country": "in",  # For India
        "apiKey": "YOUR_NEWS_API_KEY"
    }
    response = requests.get(news_base_url, params=news_params)
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get("articles", [])
        if articles:
            speaker.Speak("Here are the latest news headlines from India:")
            for i, article in enumerate(articles[:5], 1):
                title = article.get("title", "")
                if title:
                    print(f"{i}. {title}")
                    speaker.Speak(title)
        else:
            print("No news articles found.")
            speaker.Speak("Sorry, no news articles found.")
    else:
        print("Failed to fetch news:", response.status_code)
        speaker.Speak("Sorry, I couldn't fetch the latest news.")

# Function to fetch weather information using OpenWeather API
def fetch_weather():
    weather_base_url = "http://api.openweathermap.org/data/2.5/weather"
    weather_params = {
        "q": "Hyderabad",  # City name
        "appid": "YOUR_WEATHER_API_KEY",
        "units": "metric"  # For temperature in Celsius
    }
    response = requests.get(weather_base_url, params=weather_params)
    if response.status_code == 200:
        weather_data = response.json()
        main = weather_data.get("main", {})
        temperature = main.get("temp")
        description = weather_data.get("weather", [{}])[0].get("description")
        if temperature and description:
            print(f"The current temperature in Hyderabad is {temperature} degrees Celsius with {description}.")
            speaker.Speak(f"The current temperature in Hyderabad is {temperature} degrees Celsius with {description}.")
        else:
            print("Weather information not available.")
            speaker.Speak("Sorry, weather information is not available.")
    else:
        print("Failed to fetch weather information:", response.status_code)
        speaker.Speak("Sorry, I couldn't fetch the weather information.")

# Function to play a specific song from the music folder
def play_song(song_title):
    music_folder = "C:\music"  # Change this to the path of your music folder
    song_found = False
    for root, dirs, files in os.walk(music_folder):
        for file in files:
            if song_title.lower() in file.lower():
                song_path = os.path.join(root, file)
                os.startfile(song_path)
                # speaker.Speak(f"Now playing {song_title}.")
                song_found = True
                break
        if song_found:
            break
    if not song_found:
        speaker.Speak(f"Sorry, I couldn't find the song {song_title}.")

# Function to recognize user commands
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            print(e)
            return "Some error occurred, Sorry from Jarvis"

# Function to sleep Jarvis
def jarvis_sleep():
    global jarvis_sleeping
    jarvis_sleeping = True
    print("Jarvis is sleeping...")
    time.sleep(2)  # Sleep for 5 seconds to simulate Jarvis sleeping
    print("Jarvis woke up!")
    jarvis_sleeping = False

if __name__ == '__main__':
    speaker.Speak("Hello, I am Jarvis. How can I assist you today?")
    while True:
        if not jarvis_sleeping:
            print("Listening...")
            query = take_command().lower()
            print("Recognizing...")
            if "news".lower() in query.lower():
                fetch_news()
                jarvis_sleep()
            elif "weather".lower() in query.lower():
                fetch_weather()
                jarvis_sleep()
            elif "time".lower() in query.lower():
                strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                speaker.Speak(f"Sir now the time is {strfTime}")
            elif "open youtube".lower() in query.lower():
                webbrowser.open("http://youtube.com")
                speaker.Speak("Opening YouTube for you.")
                jarvis_sleep()
            elif "open wikipedia".lower() in query.lower():
                webbrowser.open("https://www.wikipedia.org/")
                speaker.Speak("Opening Wikipedia for you.")
                jarvis_sleep()
            elif "open instagram".lower() in query.lower():
                webbrowser.open("https://www.instagram.com/")
                speaker.Speak("Opening Instagram for you.")
                jarvis_sleep()
            elif "open discord".lower() in query.lower():
                webbrowser.open("Discord:")
                speaker.Speak("Opening discord for you.")
                jarvis_sleep()
            elif "open spotify".lower() in query.lower():
                webbrowser.open("Spotify:")
                speaker.Speak("Opening spotify for you.")
                jarvis_sleep()
            elif "open google".lower() in query.lower():
                webbrowser.open("https://www.google.com/")
                speaker.Speak("Opening google for you.")
            elif "play music".lower() in query.lower():
                speaker.Speak("Sure! What song would you like to listen to?")
                song_query = take_command().lower()
                play_song(song_query)
                jarvis_sleep()
            elif "exit".lower() in query.lower():
                speaker.Speak("Goodbye sir!")
                query = take_command().lower()
                play_song(query)
                exit()
