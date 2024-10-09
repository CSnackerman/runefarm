import keyboard
import time

sessions = 0
ash_of_war_key = '9'

def print_requirements():
  print('\033[1\x1b[33m--- runefarm ---\n\x1b[0m')
  print('\x1b[4mRequirements before running...\x1b[0m')
  print('  1. Pin the Palace Approach Ledge-Road Site of Grace to the first slot')
  print('  2. Maximize stat points into FTH')
  print('  3. Equip the Sacred Relic Sword')
  print('  4. Bind the 9 key to skill/ash-of-war in keyboard bindings')
  print('  4. ????')
  print('  5. Profit')

def ask_ready():
  ready = input('\nready? [\x1b[32my\x1b[0m/\x1b[31mn\x1b[0m] ')
  if(ready.lower() == 'n' or ready.lower() == 'no'):
    print('you don\'t have the right, o\' you don\'t have the right')
    exit(0)

def press_release(key: str, hold_seconds: float = 0.05):
  keyboard.press(key)
  time.sleep(hold_seconds)
  keyboard.release(key)

def fast_teleport():
  press_release('g')
  time.sleep(1)
  press_release('f')
  time.sleep(0.5)
  press_release('e')
  time.sleep(1)
  press_release('e')
  time.sleep(7)

def slow_teleport():
  press_release('g')
  time.sleep(1)
  press_release('f')
  time.sleep(0.5)
  press_release('f')
  time.sleep(0.5)
  press_release('e')
  time.sleep(1)
  press_release('e')
  time.sleep(7)

def commit_genocide():
  press_release('w', 2.5)
  press_release('a', 0.7)
  press_release('w', 2.5)
  press_release(ash_of_war_key)
  time.sleep(5)

try:
  print_requirements()
  ask_ready()
  print('\nfarming runes...')

  time.sleep(7) # time allowance to refocus game window 

  slow_teleport()

  while 1:
    commit_genocide()
    sessions += 1
    fast_teleport()

except KeyboardInterrupt:
  if (sessions == 0):
    print('\nwhy is it always \033[38;5;94mdung\x1b[0m?')
    exit(0)

  print('the light has faded; it is time to rest')
  print(f'you exterminated \x1b[34m{13 * sessions} albanaurics\x1b[0m')
  print('good work, tarnished')
  exit(0)