fwdMotors.setup_driving(fwdMotors.servo1, fwdMotors.servo2, 0)

def on_forever():
    if fwdSensors.sonar1.fwd_distance_past_threshold(0.2, fwdSensors.ThresholdDirection.UNDER):
        fwdMotors.stop()
        basic.pause(1000)
        fwdMotors.drive(fwdMotors.DrivingDirection.REVERSE, 50)
        basic.pause(1000)
        if Math.random_boolean():
            fwdMotors.turn(25)
            basic.pause(1000)
        else:
            fwdMotors.turn(-25)
            basic.pause(1000)
    else:
        fwdMotors.drive(fwdMotors.DrivingDirection.FORWARD, 50)
basic.forever(on_forever)
