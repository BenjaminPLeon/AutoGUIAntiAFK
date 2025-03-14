from pyautogui import move, keyDown, keyUp
from time import sleep
from random import choice, random

print("Welcome to my pyautogui anti-AFK script")

print("what do you want the max delay between button presses to be?")
max_delay_time = input('Maxmimum Delay Time: ')

print("what do you want the maxmimum movement of the cursor to be?")
max_movement = input('Maxmimum Cursor movement: ')

print("what do you want the cursor time multiplier to be?")
cursor_time_mult = input('Cursor time multiplier: ')

print("how long do you want movement keys to be held down?")
key_hold_time = input('Key Hold Time: ')

choices = ["up", "down", "left", "right", "forward", "backwards", "mleft", "mright"]

print("Pyautogui is running anti-AFK, press CTRL-C to exit")

while 1:
    sleep(random() * float(max_delay_time))
    val = choice(choices)
    cursor_time_rand = (random() + 1 ) * float(cursor_time_mult)
    match val:
        case "up":
            move(None, (-1 * max_movement), duration=cursor_time_rand)
            move(None, max_movement, duration=cursor_time_rand)
        case "down":
            move(None, max_movement, duration=cursor_time_rand)
            move(None, (-1 * max_movement), duration=cursor_time_rand)
        case "left":
            move((-1 * max_movement), None, duration=cursor_time_rand)
            move(max_movement, None, duration=cursor_time_rand)
        case "right":
            move(max_movement, None, duration=cursor_time_rand)
            move((-1 * max_movement), None, duration=cursor_time_rand)
        case "forward":
            keyDown("w")
            sleep(key_hold_time)
            keyUp("w")
        case "backwards":
            keyDown("s")
            sleep(key_hold_time)
            keyUp("s")
        case "mleft":
            keyDown("a")
            sleep(key_hold_time)
            keyUp("a")
        case "mright":
            keyDown("d")
            sleep(key_hold_time)
            keyUp("d")
        case _:
            print("whoops")