# bounce.py
#
# Exercise 1.5
# https://github.com/wlpygit/practical-python/blob/master/Notes/01_Introduction/02_Hello_world.md

""" A rubber ball is dropped from a height of 100 meters and each time 
it hits the ground, it bounces back up to 3/5 the height it fell. Write 
a program bounce.py that prints a table showing the height of the first 
10 bounces.
 """

bounce = 0
height = 100.0

while bounce < 10:
    bounce +=1
    height = height *3/5
    print('Bounce #:', bounce, 'Height:', round(height, 4))
