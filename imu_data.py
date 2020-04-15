import numpy as np

class IMUData:
    def __init__(self, timestamp, accelX, accelY, accelZ, gyroX, gyroY, gyroZ, magX, magY, magZ):
        self.timestamp = timestamp
        self.accel = np.array([accelX, accelY, accelZ])
        self.gyro = np.array([gyroX, gyroY, gyroZ])
        self.mag = np.array([magX, magY, magZ])
    
    def __str__(self):
        return "timestamp: {}\n\
                accel:\n\tx: {}\n\ty: {}\n\tz: {}\n\
                gyro:\n\tx: {}\n\ty: {}\n\tz: {}\n\
                mag:\n\tx: {}\n\ty: {}\n\tz: {}\n".format(self.timestamp, 
                self.accel[0], self.accel[1], self.accel[2], 
                self.gyro[0], self.gyro[1], self.gyro[2], 
                self.mag[0], self.mag[1], self.mag[2])