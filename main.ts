radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        DFRobotMaqueenPlus.mototRun(Motors.ALL, Dir.CW, 100)
        basic.showIcon(IconNames.Heart)
    } else if (receivedNumber == 0) {
        DFRobotMaqueenPlus.mototStop(Motors.ALL)
        basic.showIcon(IconNames.SmallHeart)
    } else {
        basic.showIcon(IconNames.Confused)
    }
})
input.onButtonPressed(Button.A, function () {
    DFRobotMaqueenPlus.mototRun(Motors.ALL, Dir.CW, 200)
})
radio.onReceivedString(function (receivedString) {
    if (receivedString == "UP") {
        DFRobotMaqueenPlus.servoRun(Servos.S1, 45)
    } else if (receivedString == "DN") {
        DFRobotMaqueenPlus.servoRun(Servos.S1, 0)
    } else {
        basic.showIcon(IconNames.LeftTriangle)
    }
})
input.onButtonPressed(Button.B, function () {
    DFRobotMaqueenPlus.mototStop(Motors.ALL)
})
radio.onReceivedValue(function (name, value) {
    if (name == "speed") {
        s1 = DFRobotMaqueenPlus.readSpeed(Motors1.M1) + value
        s2 = DFRobotMaqueenPlus.readSpeed(Motors1.M2) + value
        d1 = DFRobotMaqueenPlus.readDirection(Motors1.M1)
        d2 = DFRobotMaqueenPlus.readDirection(Motors1.M2)
        if (d1 == 1) {
            DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CW, s1)
        } else if (d1 == 2) {
            DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CCW, s1)
        } else {
            basic.showIcon(IconNames.Angry)
        }
        if (d2 == 1) {
            DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CW, s2)
        } else if (d2 == 2) {
            DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CCW, s2)
        } else {
            basic.showIcon(IconNames.Angry)
        }
    } else if (name == "vx") {
        x = value
    } else if (name == "vy") {
        y = value
    } else {
        basic.showIcon(IconNames.StickFigure)
    }
})
let y = 0
let x = 0
let d2 = 0
let d1 = 0
let s2 = 0
let s1 = 0
DFRobotMaqueenPlus.I2CInit()
radio.setGroup(127)
DFRobotMaqueenPlus.mototStop(Motors.ALL)
basic.showIcon(IconNames.SmallHeart)
