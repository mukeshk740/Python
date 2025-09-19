#importing OS library, required to interact with base OS.
import os
#importing pyttsx3 library, required for text to speak functionality
import pyttsx3
#Startup Announcement, it will speak the lines given

engine = pyttsx3.init()
engine.say("welcome to my program !! You can Chat with me your requirements !! or type quit ")
engine.runAndWait()
# Infinite loop, to run the program continuously
while True:
    print("Chat with me your requirements:", end=' ')
    x = input()
    p = x.upper()

    if (("RUN" in p) or ("OPEN" in p) or ("EXECUTE" in p)) and (("NOTEPAD" in p) or ("TEXT EDITOR" in p)):
        os.system("gedit")   # Opens gedit (Linux text editor)
    elif (("RUN" in p) or ("OPEN" in p) or ("EXECUTE" in p)) and (("CHROME" in p) or ("GOOGLE CHROME" in p)):
        os.system("google-chrome")  # Opens Chrome
    elif ("EXIT" in p) or ("QUIT" in p):
        break
    else:
        print("Functionality not available")