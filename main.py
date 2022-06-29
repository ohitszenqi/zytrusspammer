# -- Discord Spammer
import colorama
import keyboard
import pyautogui
from colorama import Fore
import sys

statement = False
st = False
def stop():
    if keyboard.is_pressed('f10'):
        return True


def spam(msg):
  while True:
      print(statement)
      if not statement:
          pyautogui.write(msg)
          pyautogui.press('Enter')
      if stop():
          print("[Z] Spamming stopped.")
          break


print(Fore.RED, "[Z] What to spam: ", end='')
text = input()
print(Fore.YELLOW, "[Z] Press F9 to start spamming")

while True:
    if not st:
        if keyboard.is_pressed('f9'):
            st = True

