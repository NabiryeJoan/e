import speech_recognition as sr

def detect_men_sound():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening for speech...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio)

        if "men" in text.lower():
            print("Men sound detected!")
        else:
            print("No men sound detected.")

    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Error occurred while making the request: {e}")

if __name__ == "__main__":
    detect_men_sound()