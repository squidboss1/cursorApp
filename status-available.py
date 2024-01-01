import pyautogui
import time
import threading
import random
import keyboard
import sys

exit_flag = threading.Event()


def move_cursor():
    screen_width, screen_height = pyautogui.size()
    x = random.randint(0, screen_width)
    y = random.randint(150, screen_height - 150)
    pyautogui.moveTo(x, y, duration=0.9)


def move_cursor_with_click():
    move_cursor()
    pyautogui.click()


def cursor_only_loop():
    global exit_flag
    while not exit_flag.is_set():
        move_cursor()
        time.sleep(7)


def cursor_with_click_loop():
    global exit_flag
    while not exit_flag.is_set():
        move_cursor_with_click()


def check_exit_key():
    global exit_flag
    while not exit_flag.is_set():
        if keyboard.is_pressed('esc'):
            exit_flag.set()
            break
        if keyboard.is_pressed('q'):
            exit_flag.set()
            break


if __name__ == "__main__":
    try:
        print("""
        
          aaaaaaaa
         a        a
        a          a
       a        a   a
       a   a   a    a
       a    a a     a
        a    a     a
         a        a
          aaaaaaaa
           
        Status-Available
        v.0.3p

        Maximize window and go for a coffee :)
        \n
        """)

        while True:
            print("Menu:")
            print("1) Move cursor only (no clicks)")
            print("2) Move cursor with clicks")
            print("3) Exit [Press 'Esc' or 'q']")

            choice = input("Enter your choice: ")
            if choice == '1':
                exit_flag.clear()
                threading.Thread(target=cursor_only_loop).start()
                threading.Thread(target=check_exit_key).start()
                while not exit_flag.is_set():
                    if keyboard.is_pressed('esc') or keyboard.is_pressed('q'):
                        exit_flag.set()
                        break
                sys.exit()
            elif choice == '2':
                exit_flag.clear()
                threading.Thread(target=cursor_with_click_loop).start()
                threading.Thread(target=check_exit_key).start()
                while not exit_flag.is_set():
                    if keyboard.is_pressed('esc') or keyboard.is_pressed('q'):
                        exit_flag.set()
                        break
                sys.exit()
            elif choice == '3':
                print("Exiting the script.")
                sys.exit()
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
                continue

    except KeyboardInterrupt:
        print("\nScript interrupted.")

