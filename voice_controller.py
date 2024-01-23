import logging
import pyautogui
import pyttsx3
from nltk import word_tokenize
import speech_recognition as sr
import os  # Import the os module for playing audio
from mouse_actions import MouseActions

import sys
sys.path.append('/path/to/modules_directory')



class VoiceController:
    def __init__(self, language='sv-SE'):
        self.speech_recognizer = sr.SpeechRecognizer()
        self.language = language
        self.engine = pyttsx3.init()  # Initialize the text-to-speech engine
        self.mouse_actions = MouseActions()
        self.setup_logging()

    def setup_logging(self):
        # Configure logging
        logging.basicConfig(filename='voice_controller.log', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')


    def run(self):
        try:
            while True:
                command = self.listen()
                if command == "exit":
                    self.speak("Exiting the application.")
                    break
                processed_command = self.process_command(command)
                self.execute_command(processed_command)
                self.speak("Command executed.")
        except KeyboardInterrupt:
            self.speak("Application interrupted.")
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
        finally:
            self.cleanup()

  
    def speak(self, text):
        """Use text-to-speech to say something."""
        self.engine.say(text)
        self.engine.runAndWait()


    def listen(self):
        """Listen for voice commands and recognize them."""
        with sr.Microphone() as source:
            print(f"Listening... (Language: {self.language})")
            logging.info("Listening for a command...")
            audio = self.speech_recognizer.listen(source)
            try:
                command = self.speech_recognizer.recognize_google(audio, language=self.language).lower()
                print(f"You said: {command}")
                logging.info(f"User command: {command}")
                return command
            except sr.UnknownValueError:
                print("Sorry, I did not get that.")
                logging.warning("UnknownValueError: Could not recognize the command.")
            except sr.RequestError as e:
                print(f"Speech recognition request error: {e}")
                logging.error(f"Speech recognition request error: {e}")
            return None


    def process_command(self, command):
        """
        Process the command using NLP.
        Here you can add more sophisticated NLP processing.
        """
        tokens = word_tokenize(command)
        # Ytterligare bearbetning baserad på tokens (Further processing based on tokens)
        # ...
        return command  # Return the processed command (modify this as you develop your NLP processing)



    def execute_command(self, command):
        """Execute the command by simulating mouse movements or clicks."""
        if command.startswith("move"):
            self.mouse_actions.execute_mouse_action(command)
        elif command == "click":
            self.mouse_actions.click()
        else:
            self.text_to_speech.speak("Command not recognized")


    def move_left(self):
        pyautogui.move(-100, 0)
        self.speak("Flyttar åt vänster")  # Moving left

    def move_right(self):
        pyautogui.move(100, 0)
        self.speak("Flyttar åt höger")  # Moving right

    def move_up(self):
        pyautogui.move(0, -100)
        self.speak("Flyttar upp")  # Moving up

    def move_down(self):
        pyautogui.move(0, 100)
        self.speak("Flyttar ner")  # Moving down

    def click(self):
        pyautogui.click()
        self.speak("Klickar")  # Click

    # ... other action methods ...

    def cleanup(self):
        logging.info("Voice Controller is shutting down.")
        self.recognizer.__exit__(None, None, None)


if __name__ == "__main__":
    vc = VoiceController(language='sv-SE')  # Set the desired language here
    try:
        while True:
            command = vc.listen()
            if command == "exit":
                break
            processed_command = vc.process_command(command)
            vc.execute_command(processed_command)
            vc.speak("Command executed.")
    except KeyboardInterrupt:
        pass  # Handle Ctrl+C gracefully
    finally:
        vc.cleanup()


