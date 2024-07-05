# J.A.R.V.I.S - Desktop Voice Assistant

## Overview

J.A.R.V.I.S (Just A Rather Very Intelligent System) is a desktop voice assistant built using Python. This project showcases various skills in Python development and the utilization of multiple libraries to create a fully functional, interactive voice assistant. The assistant can fetch news, provide weather updates, play music, open various websites, and more, all through voice commands. This project is a demonstration of my ability to integrate different APIs and libraries to create a seamless and user-friendly experience.

## Features

1. **Voice Interaction**: J.A.R.V.I.S interacts with users through voice commands and responses, providing a hands-free experience.
2. **Fetch News**: It fetches the latest news headlines from India using the News API.
3. **Weather Updates**: It provides current weather information for Hyderabad using the OpenWeather API.
4. **Music Playback**: It can play specific songs from the user's local music folder.
5. **Open Websites**: It can open various popular websites like YouTube, Wikipedia, Instagram, Discord, Spotify, and Google on voice command.
6. **Time Updates**: It can tell the current time.
7. **Sleep Mode**: The assistant can go into a temporary sleep mode after performing a task, simulating a rest period before taking new commands.

## Technical Details

### Libraries Used

- **win32com.client**: For text-to-speech functionality, allowing J.A.R.V.I.S to respond to users with voice.
- **speech_recognition (sr)**: To recognize and process voice commands from the user.
- **requests**: For making HTTP requests to external APIs (News API and OpenWeather API).
- **webbrowser**: To open web pages in the default browser.
- **os**: For interacting with the operating system, such as opening files.

### APIs Utilized

- **News API**: Provides the latest news headlines.
- **OpenWeather API**: Provides current weather information.

### Functionality Breakdown

1. **fetch_news()**:
   - Fetches the latest news headlines from India.
   - Uses the News API to get news data.
   - Reads out the top 5 news headlines.

2. **fetch_weather()**:
   - Provides current weather information for Hyderabad.
   - Uses the OpenWeather API to get weather data.
   - Reads out the current temperature and weather description.

3. **play_song(song_title)**:
   - Plays a specific song from the user's local music folder.
   - Searches for the song by title and plays it if found.

4. **take_command()**:
   - Listens to the user's voice command.
   - Uses Google's speech recognition to convert voice to text.

5. **jarvis_sleep()**:
   - Puts J.A.R.V.I.S into a sleep mode for 2 seconds to simulate rest.

6. **Main Loop**:
   - Continuously listens for voice commands.
   - Executes corresponding functions based on recognized commands.
   - Can perform actions like fetching news, providing weather updates, playing music, opening websites, telling time, and entering sleep mode.

## Installation and Setup

1. Clone the repository to your local machine.
2. Install the required Python libraries using:
   ```bash
   pip install pywin32 SpeechRecognition requests
3. Replace the API keys in the `fetch_news` and `fetch_weather` functions with your own keys from News API and OpenWeather API, respectively.
4. Set the path to your local music folder in the `play_song` function.
5. Run the script using Python:
    ```bash
    python jarvis.py

## Usage

- Run the script and J.A.R.V.I.S will greet you.
- Give voice commands like "news", "weather", "play music", "open YouTube", etc.
- J.A.R.V.I.S will respond to your commands and perform the requested actions.
- To exit the program, say "exit".

## Conclusion

J.A.R.V.I.S is a robust and interactive desktop voice assistant that demonstrates my proficiency in Python development and the integration of various libraries and APIs. It provides a hands-free way to access news, weather updates, play music, and open websites, enhancing the user's productivity and convenience.

