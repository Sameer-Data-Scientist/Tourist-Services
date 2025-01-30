import googletrans as gt
import gtts as gts
import playsound as pld
import speech_recognition as spr
import os

def voice_translator():
    def voice_01(x, y):
        while True:
            try:
                recognition = spr.Recognizer()
                with spr.Microphone() as source:
                    print("Speak Now....")
                    voice = recognition.listen(source)
                    text = recognition.recognize_google(voice, language=x)
                    print("Recognized text:", text)
                translate = gt.Translator()
                translator = translate.translate(text, dest=y)
                print("Translated text:", translator.text)
                converted_audio = gts.gTTS(translator.text, lang=y)
                converted_audio.save("project.mp3")
                pld.playsound("project.mp3")
                os.remove("project.mp3")
            except spr.UnknownValueError:
                print(" Speech is not clear.")
            except spr.RequestError:
                print("Unable to reach the recognition service.")
            except Exception as e:
                print("An unexpected error occurred:", e)
            n = input(" Do you want to Continue....( Y/N)").lower()
            if n == "n":
                return "***************(End)***************"
                break

    print("Hello To Voice Translator ".center(110, "-"))
    c = "View Language Code's :\n"
    print(c, gt.LANGUAGES)
    print("~" * 100)
    d = input("Start or Not  ").lower()
    if d == "s" or d == "start" or d == "y" or d == "yes":
        a = input("Select Your Language Code")
        b = input("Select Destination Language Code ")
        print(voice_01(a, b))
    else:
        print(" Tap to Start ".center(100, "-"))


