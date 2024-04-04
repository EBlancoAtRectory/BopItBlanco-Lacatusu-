import random as rn
from sense_hat import SenseHat
import time
print ("Hi mrs Karp")

sense = SenseHat()
a = (255,255,255)
b = (0,0,0)
arrows = [[
a,a,a,b,b,a,a,a,
a,a,b,b,b,b,a,a,
a,b,b,b,b,b,b,a,
a,a,a,b,b,a,a,a,
a,a,a,b,b,a,a,a,
a,a,a,b,b,a,a,a,
a,a,a,b,b,a,a,a,
a,a,a,b,b,a,a,a,
],[
a,a,a,b,b,a,a,a,
a,a,a,b,b,a,a,a,
a,a,a,b,b,a,a,a,
a,a,a,b,b,a,a,a,
a,a,a,b,b,a,a,a,
a,b,b,b,b,b,b,a,
a,a,b,b,b,b,a,a,
a,a,a,b,b,a,a,a,
],[
a,a,a,a,a,a,a,a,
a,a,a,a,a,b,a,a,
a,a,a,a,a,b,b,a,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
a,a,a,a,a,b,b,a,
a,a,a,a,a,b,a,a,
a,a,a,a,a,a,a,a,
],[
a,a,a,a,a,a,a,a,
a,a,b,a,a,a,a,a,
a,b,b,a,a,a,a,a,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
a,b,b,a,a,a,a,a,
a,a,b,a,a,a,a,a,
a,a,a,a,a,a,a,a,
],[
a,a,b,b,b,b,a,a,
a,b,b,b,b,b,b,a,
b,b,b,b,b,b,b,b,
b,b,b,a,a,b,b,b,
b,b,b,a,a,b,b,b,
b,b,b,b,b,b,b,b,
a,b,b,b,b,b,b,a,
a,a,b,b,b,b,a,a,]]

count = ['up','down','right','left','middle']
x = rn.randint(0,4)
sense.set_pixels(arrows[x])
game = 1
score = 0
while(game == 1):

limit = 5
s = time.time()
event = sense.stick.wait_for_event()
e = time.time()
t = (e-s)


if t<limit and event.action == "pressed" and event.direction == count[x]:
x = rn.randint(0,4)
sense.set_pixels(arrows[x])
score = score + 1
elif event.action == "pressed" and t>limit:
game = 0
print("Game over. Time's up.")
elif event.action == "pressed" and event.direction != count[x]:
sense.clear(255,0,0)
game = 0
print("Game over. Wrong direction. No rizz.")

if game != 1:
print("Your score was..." + str(score) + " points.")







