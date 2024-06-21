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

    def createTodo(self):
        pass

# Further / automatic responses
# Search Querying

# Music Control

# Todo List

# Navigation

# Notifications