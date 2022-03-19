def on_received_number(receivedNumber):
    basic.show_number(receivedNumber)
    if receivedNumber == 1:
        DFRobotMaqueenPlus.motot_run(Motors.ALL, Dir.CW, 100)
        basic.show_icon(IconNames.HEART)
    elif receivedNumber == 0:
        DFRobotMaqueenPlus.motot_stop(Motors.ALL)
        basic.show_icon(IconNames.SMALL_HEART)
    else:
        basic.show_icon(IconNames.CONFUSED)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    DFRobotMaqueenPlus.motot_run(Motors.ALL, Dir.CW, 200)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    basic.show_icon(IconNames.LEFT_TRIANGLE)
    if receivedString == "UP":
        DFRobotMaqueenPlus.servo_run(Servos.S1, 45)
    elif receivedString == "DN":
        DFRobotMaqueenPlus.servo_run(Servos.S1, 0)
    else:
        basic.show_icon(IconNames.CHESSBOARD)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    DFRobotMaqueenPlus.motot_stop(Motors.ALL)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_value(name, value):
    global s1, s2, d1, d2, x, y
    basic.show_icon(IconNames.SILLY)
    if name == "speed":
        s1 = DFRobotMaqueenPlus.read_speed(Motors1.M1) + value
        s2 = DFRobotMaqueenPlus.read_speed(Motors1.M2) + value
        d1 = DFRobotMaqueenPlus.read_direction(Motors1.M1)
        d2 = DFRobotMaqueenPlus.read_direction(Motors1.M2)
        if d1 == 1:
            DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, s1)
        elif d1 == 2:
            DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CCW, s1)
        else:
            basic.show_icon(IconNames.ANGRY)
        if d2 == 1:
            DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, s2)
        elif d2 == 2:
            DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CCW, s2)
        else:
            basic.show_icon(IconNames.ANGRY)
    elif name == "vx":
        x = value
    elif name == "vy":
        y = value
    else:
        basic.show_icon(IconNames.STICK_FIGURE)
radio.on_received_value(on_received_value)

y = 0
x = 0
d2 = 0
d1 = 0
s2 = 0
s1 = 0
DFRobotMaqueenPlus.i2c_init()
radio.set_group(127)
radio.set_transmit_serial_number(True)
DFRobotMaqueenPlus.motot_stop(Motors.ALL)
basic.show_icon(IconNames.SMALL_HEART)