let deg = 0
let servo = 0
let cmd = ""
serial.setBaudRate(BaudRate.BaudRate115200)
serial.writeLine("hello kibo")
basic.showIcon(IconNames.Heart)
basic.forever(function () {
    cmd = serial.readUntil(serial.delimiters(Delimiters.NewLine))
    if (cmd.length != 2) {
        serial.writeLine("length: " + cmd.length)
    } else {
        servo = parseInt(cmd[0])
    }
    if (!(cmd.isEmpty())) {
        if (cmd.substr(0, 2).includes("S ")) {
            servo = parseInt(cmd.substr(2, 1))
            deg = parseInt(cmd.substr(4, 8))
            if (servo >= 0 && servo < 6 && deg >= 0 && deg <= 180) {
                Servo.Servo(servo, deg)
            }
        } else {
            serial.writeLine("unknown command: " + cmd)
        }
    }
})
