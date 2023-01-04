import pyautogui as pt
from time import sleep
import random

# red heart color value = (255, 0, 82); found from running the heart_color.py file. 

class GuiCommand:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def navigate_to_heart(self, speed):
        # # Find the position of the 'bookmark.png' image on the screen
        position = pt.locateOnScreen('bookmark.png', confidence=.8)
        
        # Calculate the x and y coordinates of the 
        # heart based on the position of the 'bookmark.png' image
        self.x = position[0] - 405
        self.y = position[1] + 10

        # Move the mouse cursor to the heart
        pt.moveTo(self.x, self.y, duration=speed)
        print('Navigating to heart...')
        # Sleep for a random amount of time to add some variability
        sleep(random.uniform(.3, .7))



commands = GuiCommand(0, 0)

for i in range(0, 100):
    try:
        commands.navigate_to_heart(.1)
        # Check if the current pixel color matches the color of the heart (255, 0, 88)
        # If it does, it means that the heart is red, and it's already been liked
        # so we scroll down without clicking
        if pt.pixelMatchesColor(pt.position().x, pt.position().y, (255, 0, 88), tolerance=10):
            pt.scroll(-500)
            sleep(random.uniform(.3, .9))

        else:
            # If the heart is not red, then click on it
            # and scroll down
            pt.click()
            print('Heart clicked!')
            sleep(random.uniform(.2, 1.5))
            pt.scroll(-500)

    except Exception as e:
        print(e)
        pt.scroll(-500)
        sleep(random.uniform(.7, 2.0))

