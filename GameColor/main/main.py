import random
from time import sleep
from gpiozero import Button, LED

"""Level of the game"""
#level = 3

"""Button enter"""
btnEnter = Button(26)

"""All leds"""
leds = {
    1: LED(22),     #Blue
    2: LED(5),      #Red
    3: LED(4),      #Yellow
    4: LED(17),     #Green
    5: LED(27)      #White
}

"""All color buttons"""
buttons = {
    1: Button(18),  #Blue
    2: Button(23),  #Red
    3: Button(24),  #Yellow
    4: Button(25),  #Green
    5: Button(12)   #White
}

"""Function for play one led"""
def play_led(led, duration=0.5):
    led.on()
    sleep(duration)
    led.off()
    sleep(0.2)

"""Function for play the patern of the led"""
def play_pattern(pattern):
    for number in pattern:
        print(number)
        play_led(leds[number])

"""Function for save the player answer"""
def get_player_answer():
    player_answer = []
    while not btnEnter.is_pressed:
        for number, button in buttons.items():
            if button.is_pressed:
                play_led(leds[number], 0.1)
                player_answer.append(number)
    return player_answer

"""Function for check the answer of the player"""
def check_answer(solution, player_answer, level):
    print(player_answer)
    if player_answer == solution:
        level += 1
        print(f"GG, next level is {level}, Continue ?")
        play_led(leds[4])
        btnEnter.wait_for_press()
        return [level, True]
    else:
        print("You lost")
        play_led(leds[2])
        btnEnter.wait_for_press()
        return [level, False]

"""Function for controls the program"""
def main(level):
    pattern = [random.randint(1, 5) for _ in range(level)]
    play_pattern(pattern)
    player_answer = get_player_answer()
    return check_answer(pattern, player_answer, level)

"""While for play the program in a loop
while True:
    main(level)
"""