
class IMUData:
    def __init__(self, timestamp, accelX, accelY, accelZ, gyroX, gyroY, gyroZ, magX, magY, magZ):
        self.timestamp = timestamp
        self.accelX = accelX
        self.accelY = accelY
        self.accelZ = accelZ
        self.gyroX = gyroX
        self.gyroY = gyroY
        self.gyroZ = gyroZ
        self.magX = magX
        self.magY = magY
        self.magZ = magZ
    
    def __str__(self):
        return "timestamp: {}\n\
                accel:\n\tx: {}\n\ty: {}\n\tz: {}\n\
                gyro:\n\tx: {}\n\ty: {}\n\tz: {}\n\
                mag:\n\tx: {}\n\ty: {}\n\tz: {}\n".format(self.timestamp, 
                self.accelX, self.accelY, self.accelZ, 
                self.gyroX, self.gyroY, self.gyroZ, 
                self.magX, self.magY, self.magZ)
                