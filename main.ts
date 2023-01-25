input.onButtonPressed(Button.A, function () {
    basic.showString("" + (randint(0, 1000)))
})
input.onGesture(Gesture.Shake, function () {
    basic.showString("" + (input.temperature()))
    basic.showString("ºC")
})
input.onButtonPressed(Button.AB, function () {
    basic.showString("Farmacias Chanquete")
    for (let index = 0; index < 4; index++) {
        basic.showLeds(`
            . . # . .
            . . # . .
            # # # # #
            . . # . .
            . . # . .
            `)
        basic.pause(50)
        basic.showLeds(`
            . . . # .
            # # . # .
            . . # . .
            . # . # #
            . # . . .
            `)
        basic.pause(10)
        basic.showLeds(`
            . # . . .
            . # . # #
            . . # . .
            # # . # .
            . . . # .
            `)
        basic.pause(10)
        basic.showLeds(`
            . . # . .
            . . # . .
            # # # # #
            . . # . .
            . . # . .
            `)
        basic.pause(100)
        basic.showLeds(`
            . . . . .
            . . # . .
            . # # # .
            . . # . .
            . . . . .
            `)
    }
    basic.clearScreen()
    basic.pause(100)
    basic.showString("24H")
    basic.pause(100)
    basic.showString("" + (input.temperature()))
    basic.showString("ºC")
    basic.pause(1000)
})
input.onButtonPressed(Button.B, function () {
	
})
basic.forever(function () {
	
})
