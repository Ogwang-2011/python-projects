import speech_recognition as sr
from selenium import webdriver

class voice:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.listenOnMic()

    def listenOnMic(self):
        while True:
            try:
             with sr.Microphone() as source:
                audio = self.recognizer.listen(source)
                command = self.recognizer.recognize_google(audio).lower()
                
                if "search" in command:
                    search_query = command.replace("search", "")
                    print(f"Searching for: {search_query}")
                    driver = webdriver.Chrome()
                    driver.get(f"https://www.google.com/search?q={search_query}")
                elif "exit" in command:
                    print("Exiting the voice bot.")
                    break
                else:
                    print("Command not recognized. Please say 'search' followed by your query or 'exit' to quit.")
                print(command)
            except sr.UnknownValueError:
                print("Sorry, I did not understand that. Please try again.")


listener = voice()




