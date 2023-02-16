import wpilib as wp
import rev

class Robot(wp.TimedRobot):
    def robotInit(self):
        self.motor = rev.CANSparkMax(2, rev.CANSparkMax.MotorType.kBrushless)
        self.turn = rev.CANSparkMax(3, rev.CANSparkMax.MotorType.kBrushless)
        self.turnEnconder = self.turn.getAbsoluteEncoder(rev.SparkMaxAbsoluteEncoder.Type.kDutyCycle)
        self.controller = wp.XboxController(0)

    
    def teleopPeriodic(self):
       
        motorSpeed = self.controller.getRawAxis(1)
        motorTurnSpeed = self.controller.getRawAxis(0)
        if motorSpeed < 0.05:
            motorSpeed = 0
        if motorTurnSpeed < 0.05:
            motorTurnSpeed = 0
        self.motor.set(motorSpeed)
        self.turn.set(motorTurnSpeed)
    def robotPeriodic(self):
        print(self.turnEnconder.getPosition())

    
if __name__ == '__main__':
    wp.run(Robot)
