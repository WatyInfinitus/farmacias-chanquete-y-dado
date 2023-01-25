def on_button_pressed_a():
    basic.show_string("" + str((randint(0, 1000))))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_string("" + str((input.temperature())))
    basic.show_string("ºC")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    basic.show_string("Farmacias Chanquete")
    for index in range(4):
        basic.show_leds("""
            . . # . .
                        . . # . .
                        # # # # #
                        . . # . .
                        . . # . .
        """)
        basic.pause(50)
        basic.show_leds("""
            . . . # .
                        # # . # .
                        . . # . .
                        . # . # #
                        . # . . .
        """)
        basic.pause(10)
        basic.show_leds("""
            . # . . .
                        . # . # #
                        . . # . .
                        # # . # .
                        . . . # .
        """)
        basic.pause(10)
        basic.show_leds("""
            . . # . .
                        . . # . .
                        # # # # #
                        . . # . .
                        . . # . .
        """)
        basic.pause(100)
        basic.show_leds("""
            . . . . .
                        . . # . .
                        . # # # .
                        . . # . .
                        . . . . .
        """)
    basic.clear_screen()
    basic.pause(100)
    basic.show_string("24H")
    basic.pause(100)
    basic.show_string("" + str((input.temperature())))
    basic.show_string("ºC")
    basic.pause(1000)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    pass
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)
