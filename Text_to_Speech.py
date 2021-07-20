#importing pyttsx library
import pyttsx3

#Initialization 
object = pyttsx3.init()
rep = True
while rep == True:
	#Input
	sentence1 = input("Enter Your sentence1 : ")
	sentence2 = input("Enter Your sentence2 : ")
	sentence3 = input("Enter Your sentence3 : ")
	#Testing
	object.say(sentence1)
	object.say(sentence2)
	object.say(sentence3)
	object.runAndWait()
	again = input("Continue ? 'Y' or 'N' : ")
	if again.lower() == 'n':
		Print ("Thank You")
		rep = False