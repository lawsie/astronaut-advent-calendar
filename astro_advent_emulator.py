from sense_hat import *
from time import sleep

sense = SenseHat()
#sense.set_rotation(270)

# Astronaut's advent calendar

# Remap the keys
FLIGHT_UP = DIRECTION_UP
FLIGHT_DOWN = DIRECTION_DOWN
FLIGHT_LEFT = DIRECTION_LEFT
FLIGHT_RIGHT = DIRECTION_RIGHT
FLIGHT_ENTER = DIRECTION_MIDDLE

# Colours
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

# Calendar
calendar = [ [1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1]
           ]
        


# Joystick coordinates
xcoord = 0
ycoord = 0

# Pictures
all_pics = ["e,e,e,r,r,e,e,e,e,e,r,e,e,r,e,e,e,e,e,e,e,r,e,e,e,e,e,e,r,e,e,e,e,e,e,r,e,e,e,e,e,e,e,r,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,r,e,e,e,e",
"e,g,g,e,e,g,g,e,e,e,g,r,r,g,e,e,e,e,w,w,w,w,e,e,e,w,n,w,n,n,w,e,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,e,n,n,n,n,n,n,e,e,e,n,n,n,n,e,e",
"e,e,e,v,v,e,e,e,e,e,e,v,v,e,e,e,e,e,v,y,v,y,e,e,e,v,y,v,y,v,y,e,e,y,v,y,v,y,v,e,e,v,y,v,y,v,y,e,e,y,v,y,v,y,v,e,e,e,y,v,y,v,e,e",
"e,e,e,g,g,g,e,e,e,e,g,g,g,e,g,e,e,w,w,w,w,w,e,w,n,n,b,n,b,n,n,e,e,n,n,n,n,n,e,e,e,n,n,v,n,n,e,e,e,e,n,n,n,e,e,e,e,g,g,g,g,g,e,e",
"e,e,g,e,e,e,e,e,e,e,g,g,e,e,e,e,e,g,g,e,e,e,e,g,e,e,g,g,e,g,g,g,e,g,g,e,g,g,g,e,e,e,g,g,g,g,g,e,e,e,r,r,g,e,e,e,e,e,r,r,e,e,e,e",
"e,e,e,g,g,e,e,e,e,e,g,i,g,g,e,e,e,g,g,g,g,g,g,e,e,e,g,g,g,g,e,e,e,g,g,g,g,i,g,e,g,g,i,g,g,g,g,g,e,e,e,o,o,e,e,e,e,e,e,o,o,e,e,e",
"e,e,e,r,r,r,e,e,e,e,r,r,r,e,r,e,e,w,w,w,w,w,e,w,e,n,b,n,b,n,e,e,e,n,n,w,n,n,e,e,e,n,w,v,w,n,e,e,e,e,w,w,w,e,e,e,e,r,r,r,r,r,e,e",
"e,e,e,e,e,w,r,e,e,e,e,e,r,e,e,w,e,e,e,e,e,e,r,r,e,e,e,e,e,w,w,e,e,e,e,e,r,r,e,e,e,e,e,w,w,e,e,e,e,e,r,r,e,e,e,e,e,w,w,e,e,e,e,e",
"e,i,e,e,e,e,e,e,i,i,e,i,e,e,e,e,e,e,i,o,i,e,e,e,e,i,o,i,o,i,e,e,e,e,i,o,i,o,i,e,e,e,e,i,o,i,e,e,e,e,e,e,i,e,i,i,e,e,e,e,e,e,i,e",
"e,e,e,e,y,e,e,e,e,e,y,y,y,y,y,e,e,e,e,y,y,y,e,e,e,e,e,y,e,y,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,i,e,i,e,i,e,e,n,n,n,n,n,n,n,n",
"w,e,w,w,w,e,w,e,e,w,e,w,e,w,e,e,w,e,w,w,w,e,w,e,w,w,w,w,w,w,w,e,w,e,w,w,w,e,w,e,e,w,e,w,e,w,e,e,w,e,w,w,w,e,w,e,e,e,e,e,e,e,e,e",
"e,g,e,e,e,e,g,e,e,e,g,g,g,g,e,e,e,r,r,g,g,r,r,e,e,r,r,g,g,r,r,e,e,g,g,g,g,g,g,e,e,g,g,g,g,g,g,e,e,r,r,g,g,r,r,e,e,r,r,g,g,r,r,e",
"e,e,e,o,e,e,e,e,e,e,e,o,y,e,e,e,e,e,e,e,o,e,e,e,e,e,e,w,w,e,e,e,e,e,e,w,w,e,e,e,e,e,e,w,w,e,e,e,e,e,e,w,w,e,e,e,e,e,e,w,w,e,e,e",
"n,n,e,e,e,e,n,n,e,n,e,e,e,e,n,e,e,n,n,e,e,n,n,e,e,e,n,n,n,n,e,e,e,e,n,i,i,n,e,e,e,e,n,n,n,n,e,e,e,e,n,n,n,n,e,e,e,e,e,r,r,e,e,e",
"e,e,e,g,e,e,e,e,e,e,g,e,g,e,e,e,e,e,g,e,e,g,e,e,e,g,e,e,e,g,e,e,e,w,e,e,e,e,g,e,e,w,w,e,e,g,w,e,e,e,e,e,e,e,w,e,e,e,e,e,e,e,e,e",
"e,e,n,n,e,e,e,e,e,n,i,n,e,e,e,e,o,w,n,n,n,e,e,e,e,w,n,n,n,n,e,e,e,r,r,n,n,n,e,e,e,e,r,r,n,n,n,n,e,e,o,e,r,e,n,n,e,o,e,o,e,e,e,e",
"e,e,e,g,g,g,g,e,e,e,g,g,g,g,e,w,e,r,r,r,r,r,r,e,e,e,w,w,w,w,e,e,e,w,i,w,i,w,w,e,e,w,w,o,w,w,w,e,e,e,w,w,w,w,e,e,e,e,e,w,w,e,e,e",
"e,e,e,e,e,e,e,e,e,e,g,e,e,g,e,e,g,e,g,g,e,g,e,e,e,g,g,g,g,g,g,g,e,g,g,g,g,g,g,e,e,g,n,n,n,n,g,e,n,n,i,n,i,n,n,n,e,n,n,n,n,n,n,e",
"e,e,e,e,e,e,e,e,e,e,e,e,e,e,y,v,e,e,e,e,e,g,b,i,e,e,e,r,r,r,r,r,e,r,r,r,r,r,r,r,e,e,r,r,r,r,r,r,y,e,r,e,e,e,r,e,e,y,y,y,y,y,y,y",
"e,e,y,y,y,y,e,e,e,e,e,n,n,e,e,e,e,e,e,n,n,e,e,e,e,y,y,w,w,y,y,e,e,e,y,w,w,y,e,e,e,e,e,w,w,e,e,e,e,e,w,w,w,w,e,e,e,w,w,w,w,w,w,e",
"e,e,e,e,e,e,e,e,e,g,g,e,e,g,g,e,e,e,g,g,g,g,e,e,e,e,y,r,r,y,e,e,y,y,y,y,y,y,y,y,y,y,y,e,e,y,y,y,e,y,y,e,e,y,y,e,e,e,e,e,e,e,e,e",
"e,n,n,e,n,n,e,e,e,e,n,e,n,e,e,e,e,w,w,w,w,w,w,e,e,o,o,o,w,w,o,e,e,w,w,o,o,o,o,e,e,o,o,o,o,o,o,e,e,o,o,o,w,w,w,e,e,o,o,o,w,o,o,e",
"e,e,r,g,g,g,e,e,e,g,g,e,r,g,g,e,g,g,e,e,e,e,g,g,g,r,e,e,e,e,r,g,g,g,e,e,e,e,g,g,g,g,e,e,e,e,g,r,e,r,g,e,e,g,g,e,e,e,g,g,r,g,e,e",
"e,e,e,n,e,e,e,e,e,e,e,n,n,e,n,e,e,e,e,n,e,e,n,n,e,e,e,n,e,n,e,e,e,e,n,n,n,n,e,e,n,n,n,n,n,n,n,e,n,n,n,n,n,n,n,e,e,n,n,n,n,n,e,e",
"e,e,e,w,w,w,e,e,e,e,e,r,r,r,e,e,e,e,e,r,r,r,e,e,e,e,e,r,r,r,e,e,e,e,e,r,r,r,e,e,e,r,r,r,r,r,e,e,r,r,r,r,r,e,e,e,e,e,r,r,e,e,e,e"]


# Read the calendar from list to see which are available to be opened
def generate_cal():
    # Draw calendar
    for row in range(3):
        for col in range(8):
            if calendar[row][col] == 1:
                sense.set_pixel(col, row, colours['g'])
            else:
                sense.set_pixel(col, row, colours['i'])
    # draw joypad
    sense.set_pixel(2, 5, colours['r'])
    sense.set_pixel(4, 5, colours['r'])
    sense.set_pixel(3, 4, colours['r'])
    sense.set_pixel(3, 6, colours['r'])
    
    


# Draw the joystick position in red
def draw_joystick():
    generate_cal() # Clear first
    sense.set_pixel(xcoord, ycoord, colours['r'])

# Move joystick
def move_joystick():
    global xcoord, ycoord
    pressed = False
    while pressed == False:
        event = sense.stick.wait_for_event()
        if event.action == 'pressed' and event.direction == FLIGHT_UP:
            if ycoord > 0:
                ycoord -= 1
        elif event.action == 'pressed' and event.direction == FLIGHT_DOWN:
            if ycoord < 2:
                ycoord += 1
        elif event.action == 'pressed' and event.direction == FLIGHT_RIGHT:
            if xcoord < 7:
                xcoord += 1
        elif event.action == 'pressed' and event.direction == FLIGHT_LEFT:
            if xcoord > 0:
                xcoord -= 1
        elif event.action == 'pressed' and event.direction == FLIGHT_ENTER:
            pressed = True
            calendar[ycoord][xcoord] = 0
        draw_joystick()
        sleep(0.1)

# Figure out what day it is based on x and y coords
def get_day(x, y):
    day = y * 8 + x + 1
    return day

# Load in pictures from text file
def get_pics(day):
    try:
        return str(all_pics[day])
    except IndexError:
        # Return a ? if tried to fetch a day that doesnt exist
        return "e,e,e,r,r,e,e,e,e,e,r,e,e,r,e,e,e,e,e,e,e,r,e,e,e,e,e,e,r,e,e,e,e,e,e,r,e,e,e,e,e,e,e,r,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,r,e,e,e,e"

# Display a given picture string on the sense HAT
def display_pic(pic_string):
    pic_string = pic_string.strip()
    pic_string = pic_string.replace(",","")
    pic_string = pic_string.replace("[","")
    pic_string = pic_string.replace("]","")

    pic_list = []
    for letter in pic_string:
        pic_list.append(colours[letter])
    
    sense.set_pixels(pic_list)
    sleep(5)

    # Display special message if all 24 doors are open
    if all_open():    
        sense.show_message("Happy Christmas!")
    else:
        main()

# Check if all looked in
def all_open():
    all_done = True
    for row in calendar:
        for door in row:            
            if door == 1:
                all_done = False
    return all_done


# Main program
# ------------------------------------------
# Clear the page
def main():
    sense.clear()

    # Show the calendar
    generate_cal()

    # Show the joystick
    draw_joystick()

    # Wait for joystick movement and continue until joystick pressed (Enter)
    move_joystick()

    # Show which day it is
    today = get_day(xcoord, ycoord)
    sense.show_message( str(today) )

    # Get the picture for today as a string and display it
    picture = get_pics(today)
    display_pic(picture)

main()
