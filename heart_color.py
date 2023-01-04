"""
This code finds the red color value of the heart sign of instagram.
1. Open instagram.com
2. Click on the heart icon of any post so that the heart sign becomes red
3. Run this code
4. Then point the mouse cursor to the heart sign, this will print the color value of the heart sign
   in the terminal
5. Copy the color value and save it somewhere, so that we can use it later in the main.py file
"""

import pyautogui as pt
from time import sleep

while True:
    try:
        positionXY = pt.position()
        print(positionXY, pt.pixel(positionXY[0], positionXY[1]))
        sleep(1)

        if positionXY[0] == 0:
            break
    
    except Exception as e:
        print(e)
        pass