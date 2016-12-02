from sense_hat import *
from time import sleep

sense = SenseHat()
sense.set_rotation(270)

# Astronaut's advent calendar

# Remap the keys
FLIGHT_UP = DIRECTION_LEFT
FLIGHT_DOWN = DIRECTION_RIGHT
FLIGHT_LEFT = DIRECTION_DOWN
FLIGHT_RIGHT = DIRECTION_UP
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
    f = open("pictures.txt")
    all_pics = f.readlines()
    f.close()
    try:
        return all_pics[day]
    except IndexError:
        # Return a ? if tried to fetch a day that doesnt exist
        return "e,e,e,r,r,e,e,e,e,e,r,e,e,r,e,e,e,e,e,e,e,r,e,e,e,e,e,e,r,e,e,e,e,e,e,r,e,e,e,e,e,e,e,r,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,r,e,e,e,e"

# Display a given picture string on the sense HAT
def display_pic(pic_string):
    pic_string = pic_string.strip()
    pic_string = pic_string.replace(",","")

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
