<--------------------------------------- Welcome ------------------------------------------>

Text-to-Speech :
		Anything which you will  type will  be spoken by the computer  during the execution of 
		the Program.
 
Project description : 
 		pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries,
 		it works offline, and is compatible with both Python 2 and 3.
		
Installation:
		=> pip install pyttsx3 - (https://pypi.org/project/pyttsx3/)
		=> If you recieve errors such as No module named win32com.client, No module named win32,
			 or No module named win32api, you will need to additionally install pypiwin32.
			 
Usage :
		import pyttsx3
		engine = pyttsx3.init()
		engine.say("I will speak this text")
		engine.runAndWait()
		
<--------------------------------------- Thank You ------------------------------------------>
