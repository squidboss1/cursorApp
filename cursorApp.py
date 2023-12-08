import pyautogui
import time
import random

def move_cursor():
    screen_width, screen_height = pyautogui.size()

    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)

    pyautogui.moveTo(x, y, duration=0.5)

if __name__ == "__main__":
    try:
        print("""
        CursorApp
        v.0.1
        
        Dobrej zabawy :)
        """)

        while True:
            move_cursor()
            time.sleep(10)

    except KeyboardInterrupt:
        print("\nPrzerwano skrypt.")

