import pyautogui
import random
import time
import threading
from pynput import keyboard

pyautogui.FAILSAFE = False

stop_script = False

def on_press(key):
    global stop_script
    try:
        if key == keyboard.Key.esc:
            stop_script = True
            return False
    except Exception as e:
        print(f"Ошибка: {e}")

listener = keyboard.Listener(on_press=on_press)
listener.start()

try:
    print("Скрипт запущен. Нажми ESC для остановки.")
    screen_width, screen_height = pyautogui.size()

    while not stop_script:
        x = random.randint(0, screen_width - 1)
        y = random.randint(0, screen_height - 1)

        pyautogui.moveTo(x, y, duration=0.2)

        time.sleep(random.uniform(0.1, 0.5))

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    print("Скрипт завершен.")
