import sys
import threading
import sqlite3 as sql

import speech_recognition
import pyttsx3 as tts

from neuralintents import GenericAssistant

speechRate = 150
connection = sql.connect("wmpyaSTORE.db")
cursor = connection.cursor()
print(f"--debug - Database total changes: {connection.total_changes}")

# Main Assistant object
class Assistant:

    def __init__(self):
        # Initialisation
        self.recogniser = speech_recognition.Recognizer()
        self.speaker = tts.init()
        self.speaker.setProperty("rate", speechRate)
        self.assistant = GenericAssistant("intents.json", 
                                          intent_methods={
                                              "Todo List": self.createTodo})
        
        # DATABASE Construction
        cursor.execute("CREATE TABLE IF NOT EXISTS todo (id INTEGER PRIMARY KEY, timestamp DATETIME, name TEXT, data TEXT)")
        cursor.execute("CREATE TABLE IF NOT EXISTS notification (id INTEGER PRIMARY KEY, timestamp DATETIME, duedate DATETIME, name TEXT, details TEXT, priority INTEGER)")
        
        self.assistant.train_model()
        
        threading.Thread(target=self.runAssistant).start()

    def createTodo(self):
        pass

    def runAssistant(self):
        while True:
            try:
                with speech_recognition.Microphone() as mic:
                    self.recogniser.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = self.recogniser.listen(mic)#

                    text = self.recogniser.recognize_google_cloud(audio)
                    text.lower()

                    # The 'wake' option of choice
                    if "wmpya" or "doc" or "chief" or "wim-pee-ya" or "wim pee ya" in text:
                        audio = self.recogniser.listen(mic)
                        text = self.recogniser.recognize_google_cloud(audio)
                        text.lower()
                        if text == "thank you" or text == "shut down":
                            self.speaker.say("See you around!")
                            self.speaker.runAndWait()
                            self.speaker.stop()
                            sys.exit()
                        else:
                            if text is not None:
                                response = self.assistant.request(text)
                                if response is not None:
                                    self.speaker.say(response)
                                    self.speaker.runAndWait()
            except:
                continue

    # Further / automatic responses
    # Search Querying

    # Music Control

    # Todo List

    # Navigation

    # Notifications


Assistant()