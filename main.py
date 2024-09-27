import keyboard
import time

ash_of_war_key = '9'

def press_release(key: str, hold_seconds: float = 0.05):
  keyboard.press(key)
  time.sleep(hold_seconds)
  keyboard.release(key)

print('farming runes...')

try:
  while 1:
    time.sleep(7)
    press_release('w', 2.5)
    press_release('a', 0.7)
    press_release('w', 2.5)
    press_release(ash_of_war_key)
    time.sleep(5)
    press_release('g')
    time.sleep(1)
    press_release('f')
    time.sleep(0.5)
    press_release('e')
    time.sleep(1)
    press_release('e')
except KeyboardInterrupt:
  print('the light has faded; it is time to rest.')
  exit(0)