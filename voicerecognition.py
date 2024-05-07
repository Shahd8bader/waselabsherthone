import speech_recognition as sr
import pyautogui
import webbrowser
import time

# Function Definitions for Web Interactions
def open_website():
    url = 'https://www.absher.sa/wps/portal/individuals/Home/homepublic/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8ziDTxNTDwMTYy83Q3MjAwcw4IsTFw9TQ3dzUz0wwkpiAJJ4wCOBkD9UViUOBo4BRk5GRsYuPsbYVWAYkZBboRBpqOiIgBIR9Vv/dz/d5/L0lDUmlTUSEhL3dHa0FKRnNBLzROV3FpQSEhL2Fy/'
    webbrowser.open(url)
    print("Website opened.")

def refresh_page():
    pyautogui.hotkey('ctrl', 'r')
    print("Page refreshed.")

def close_browser():
    pyautogui.hotkey('alt', 'f4')  # This simulates pressing Alt+F4 to close the active window
    print("Browser closed.")

# Actions dictionary linking commands to functions
actions = {
    "افتح الموقع": open_website,
    "تحديث الصفحه": refresh_page,
    "اغلاق": close_browser
}

def recognize_speech(language='ar-EG'):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Calibrating for ambient noise... Please wait.")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        text = r.recognize_google(audio, language=language)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

def execute_command(command):
    command = command.strip().lower()
    action = actions.get(command)
    if action:
        action()
        print(f"Executed command: {command}")
    else:
        print(f"No action found for: {command}")

def main():
    while True:
        command = recognize_speech()
        if command:
            execute_command(command)

if __name__ == "__main__":
    main()
