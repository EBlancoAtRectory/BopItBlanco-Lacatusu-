import random as rn
from sense_hat import SenseHat
import time
#importing the libraries
print ("Hi mrs Karp")

sense = SenseHat()
a = (255,255,255)
b = (0,0,0)
#making the commands that are going to be printed in the terminal
arrows = ['''

	^
	|

''','''

	|
	v

''', '''

	-->

''','''

	<--

''','''

	middle

''']

#list of commands that i did
count = ['up','down','right','left', 'middle']
#making it random so the game is playable
x = rn.randint(0,4	)
print(arrows[x])
game = 1
score = 0
while(game == 1):
	sense.set_pixels([
a,a,a,b,b,a,a,a,
a,a,b,b,b,b,a,a,
a,b,b,b,b,b,b,a,
a,a,a,b,b,a,a,a,
a,a,a,b,b,a,a,a,
a,a,a,b,b,a,a,a,
a,a,a,b,b,a,a,a,
a,a,a,b,b,a,a,a,
])
#making a timer so the game can be actually a competitive one
	limit = 5
	s = time.time()
	event = sense.stick.wait_for_event()
	e = time.time()
	t = (e-s)


	#if you respected the conditions( time and correct comand) it is gonna count up
	if t<limit and event.action == "pressed" and event.direction == count[x]:
		x = rn.randint(0,4)
		print(arrows[x])
		score = score + 1
	#if you took too long to press or you did the wrong command that is when the game is gonna end
	elif event.action == "pressed" and t>limit:
		game = 0
		print("Game over. You took too long.")
	elif event.action == "pressed" and event.direction != count[x]:
		sense.clear(255,0,0)
		game = 0
		print("Game over. Wrong direction. No rizz.")

	#to count the score 
	if game != 1:
		print("Your score was..." + str(score) + " points.")







