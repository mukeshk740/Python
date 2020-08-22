#importing OS library, required to interact with base OS.
import os
#importing pyttsx3 library, required for text to speak functionality
import pyttsx3
#Startup Announcement, it will speak the lines given
pyttsx3.speak("welcome to my program !! You can Chat with me your requirements !! or type quit ")
# Infinite loop, to run the program continuously
while True:
	print("Chat with me your requirements:", end=' ')
	x = input()
	p = (x.upper())

	if (("RUN" in p) or ("OPEN" in p) or ("EXECUTE" in p)) and (("NOTEPAD" in p) or ("TEXT EDITOR" in p)):
	  os.system("NOTEPAD")
	elif (("RUN" in p) or ("OPEN" in p) or ("EXECUTE" in p)) and (("CHROME" in p) or ("GOOGLE CHROME" in p)):
	  os.system("chrome") 
	elif (("RUN" in p) or ("OPEN" in p) or ("EXECUTE" in p)) and (("MSPAINT" in p) or ("PAINT" in p)):
	  os.system("mspaint")
	elif (("RUN" in p) or ("OPEN" in p) or ("EXECUTE" in p)) and (("COMMAND PROMPT" in p) or ("CMD" in p)):
	  os.system("cmd")
	elif (("RUN" in p) or ("OPEN" in p) or ("EXECUTE" in p)) and (("SNIP" in p) or ("SNIPPING TOOL" in p)):
	  os.system("SnippingTool")
	elif (("RUN" in p) or ("OPEN" in p) or ("EXECUTE" in p)) and (("PUTTY" in p) or ("PUTTY" in p)):
	  os.system("putty")
	elif (("RUN" in p) or ("OPEN" in p) or ("EXECUTE" in p)) and (("Windows Explorer" in p) or ("Explorer" in p)):
	  os.system("explorer")
	elif (("RUN" in p) or ("OPEN" in p) or ("EXECUTE" in p)) and (("MEDIA PLAYER" in p) or ("WINDOWS MEDIA PLAYER" in p)):
	  os.system("wmplayer")
	elif (("RUN" in p) or ("OPEN" in p) or ("EXECUTE" in p)) and (("COMPUTER MANAGEMENT" in p) or ("COMPMGMT" in p)):
	  os.system("compmgmt")
	elif (("RUN" in p) or ("OPEN" in p) or ("EXECUTE" in p)) and (("SERVICES" in p) or ("WINDOWS SERVICES" in p)):
	  os.system("services.msc")
	elif ("EXIT" in p) or ("QUIT" in p ):
	  break
	else: 
	  print ("Functionality not available")
