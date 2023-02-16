import wpilib as wp
import rev

class Robot(wp.TimedRobot):
    def robotInit(self):
        self.motor = rev.CANSparkMax(2, rev.CANSparkMax.MotorType.kBrushless)
        self.turn = rev.CANSparkMax(3, rev.CANSparkMax.MotorType.kBrushless)
        self.controller = wp.XboxController(0)
    
    def teleopPeriodic(self):
        motorSpeed = self.controller.getRawAxis(1)
        motorTurnSpeed = self.controller.getRawAxis(0)
        self.motor.set(motorSpeed)
        self.turn.set(motorTurnSpeed)

if __name__ == '__main__':
    wp.run(Robot)
