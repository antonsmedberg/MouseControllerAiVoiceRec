from voice_controller import VoiceController

def main():
    language = 'sv-SE'  # Default language
    vc = VoiceController(language=language)
    try:
        while True:
            command = vc.listen()
            if command == "exit":
                vc.text_to_speech.speak("Exiting the application.")
                break
            elif command == "change language":
                language = 'en-US' if language == 'sv-SE' else 'sv-SE'
                vc.text_to_speech.speak(f"Language changed to {'English' if language == 'en-US' else 'Swedish'}.")
            elif command == "help":
                vc.text_to_speech.speak("You can say commands like 'move left,' 'move right,' 'click,' or 'change language.'")
            elif command == "configure language":
                vc.text_to_speech.speak("Please specify your preferred language: English or Swedish.")
                # Implement code to recognize and set the user's language preference
            else:
                vc.execute_command(command)
    except KeyboardInterrupt:
        pass  # Handle Ctrl+C gracefully
    finally:
        vc.cleanup()

if __name__ == "__main__":
    main()




