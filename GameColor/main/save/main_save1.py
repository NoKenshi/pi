import random
from time import *
from gpiozero import *
from signal import pause

level = 3
btnEnter = Button(26)

green = LED(17)
red = LED(5)
blue = LED(22)
yellow = LED(4)
white = LED(27)


def Main(level):
	randomList(level)

def randomList(level):
	tab = []
	for i in range(level):
		tab.append(random.randint(1,5))
	playRandomList(tab)

def playRandomList(patern):
	global red
	global green
	global blue
	global yellow
	global white

	for number in patern:
		if(number == 1):
			print("blue")
			blue.on()
			sleep(0.5)
			blue.off()
			sleep(0.2)
		elif(number == 2):
			print("red")
			red.on()
			sleep(0.5)
			red.off()
			sleep(0.2)
		elif(number == 3):
			print("yellow")
			yellow.on()
			sleep(0.5)
			yellow.off()
			sleep(0.2)
		elif(number == 4):
			print("green")
			green.on()
			sleep(0.5)
			green.off()
			sleep(0.2)
		else:
			print("white")
			white.on()
			sleep(0.5)
			white.off()
			sleep(0.2)
	playerPlay(patern)

def playerPlay(solution):
	global btnEnter
	global blue
	global red
	global yellow
	global green
	global white

	enter = True
	playerAnswer = []

	btnBlue = Button(18)
	btnYellow = Button(24)
	btnWhite = Button(12)
	btnGreen = Button(25)
	btnRed = Button(23)

	while enter:
		if(btnEnter.is_pressed):
			sleep(0.5)
			enter = False
		def Blue():
			playerAnswer.append(1)
			blue.on()
			sleep(0.1)
			blue.off()
		def Red():
			playerAnswer.append(2)
			red.on()
			sleep(0.1)
			red.off()
		def Yellow():
			playerAnswer.append(3)
			yellow.on()
			sleep(0.1)
			yellow.off()
		def Green():
			playerAnswer.append(4)
			green.on()
			sleep(0.1)
			green.off()
		def White():
			playerAnswer.append(5)
			white.on()
			sleep(0.1)
			white.off()

		btnBlue.when_pressed = Blue
		btnRed.when_pressed = Red
		btnYellow.when_pressed = Yellow
		btnGreen.when_pressed = Green
		btnWhite.when_pressed = White

	print(playerAnswer)
	checkAnswer(solution, playerAnswer)

def checkAnswer(solution, playerAnswer):
	global level
	global btnEnter
	global red
	global green
	a = True
	if(playerAnswer == solution):
		level+=1
		print("GG, level suivant {}, Continuez ?".format(level))
		green.on()
		sleep(0.5)
		green.off()
		while a:
			if(btnEnter.is_pressed):
				a = False
	else:
		level = 3
		print("Perdu, Continuez?")
		red.on()
		sleep(0.5)
		red.off()
		while a:
			if(btnEnter.is_pressed):
				a = False
while True:
	Main(level)
