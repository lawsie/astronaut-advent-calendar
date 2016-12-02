# A useful file for tinkering with pictures

from sense_hat import *
from time import sleep

sense = SenseHat()
sense.set_rotation(270)

colours = {
    
    'r' : [255, 0, 0],
    'o' : [255, 125, 0],
    'y' : [255, 255, 0],
    'g' : [0, 255, 0],
    'b' : [0, 0, 255],
    'i' : [75, 0, 130],
    'v' : [159, 0, 255],
    'n' : [135, 80, 22],
    'w' : [255, 255, 255],
    'e' : [0, 0, 0]  # e stands for empty/black

    }

# Blank picture code commented out so you can copy and paste in
'''
picture = """
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
"""
'''
# End blank picture

# The actual picture that will display
picture = """
e,e,n,n,e,e,e,e,
e,n,i,n,e,e,e,e,
o,w,n,n,n,e,e,e,
e,w,n,n,n,n,e,e,
e,r,r,n,n,n,e,e,
e,e,r,r,n,n,n,n,
e,e,o,e,r,e,n,n,
e,o,e,o,e,e,e,e
"""

# Display a given picture string on the sense HAT
def display_pic(pic_string):
    pic_string = pic_string.strip()
    pic_string = pic_string.replace(",","")
    pic_string = pic_string.replace("\n", "")

    pic_list = []
    for letter in pic_string:
        pic_list.append(colours[letter])
    
    sense.set_pixels(pic_list)
    for eachletter in pic_string:
        print( eachletter+",", end="")
    sleep(60)
    sense.clear()
   


display_pic(picture)


